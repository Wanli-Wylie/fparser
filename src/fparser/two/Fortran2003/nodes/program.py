class Program(BlockBase):  # R201
    """
    Fortran 2003 rule R201::

        program is program-unit
                   [ program-unit ] ...

    """

    subclass_names = []
    use_names = ["Program_Unit"]

    @show_result
    def __new__(cls, string, _deepcopy=False):
        """Wrapper around base class __new__ to catch an internal NoMatchError
        exception and raise it as an external FortranSyntaxError exception.

        :param type cls: the class of object to create
        :param string: (source of) Fortran string to parse
        :type string: :py:class:`FortranReaderBase`
        :param _deepcopy: Flag to signal whether this class is
            created by a deep copy
        :type _deepcopy: bool

        :raises FortranSyntaxError: if the code is not valid Fortran

        """
        # pylint: disable=unused-argument
        try:
            return Base.__new__(cls, string, _deepcopy=_deepcopy)
        except NoMatchError:
            # At the moment there is no useful information provided by
            # NoMatchError so we pass on an empty string.
            raise FortranSyntaxError(string, "")
        except InternalSyntaxError as excinfo:
            # InternalSyntaxError is used when a syntax error has been
            # found in a rule that does not have access to the reader
            # object. This is then re-raised here as a
            # FortranSyntaxError, adding the reader object (which
            # provides line number information).
            raise FortranSyntaxError(string, excinfo)

    def __getnewargs__(self):
        """Method to dictate the values passed to the __new__() method upon
        unpickling. The method must return a pair (args, kwargs) where
        args is a tuple of positional arguments and kwargs a dictionary
        of named arguments for constructing the object. Those will be
        passed to the __new__() method upon unpickling.

        :return: set of arguments for __new__
        :rtype: tuple[str, bool]
        """
        return (self.string, True)

    @staticmethod
    def match(reader):
        """Implements the matching for a Program. Whilst the rule looks like
        it could make use of BlockBase, the parser must not match if an
        optional program_unit has a syntax error, which the BlockBase
        match implementation does not do.

        :param reader: the fortran file reader containing the line(s)
                       of code that we are trying to match
        :type reader: :py:class:`fparser.common.readfortran.FortranFileReader`
                      or
                      :py:class:`fparser.common.readfortran.FortranStringReader`
        :return: `tuple` containing a single `list` which contains
                 instance of the classes that have matched if there is
                 a match or `None` if there is no match

        """
        content = []
        add_comments_includes_directives(content, reader)
        comments = content != []
        try:
            while True:
                obj = Program_Unit(reader)
                if obj:
                    # obj could be None if there are only Comments
                    content.append(obj)
                add_comments_includes_directives(content, reader)
                # cause a StopIteration exception if there are no more lines
                next_line = reader.next()
                # put the line back in the case where there are more lines
                reader.put_item(next_line)
        except NoMatchError:
            # Found a syntax error for this rule. Now look to match
            # (via Main_Program0) with a program containing no program
            # statement as this is optional in Fortran.
            #
            result = BlockBase.match(Main_Program0, [], None, reader)
            if not result and comments:
                # This program only contains comments.
                return (content,)
            else:
                return result
        except StopIteration:
            # Reader has no more lines.
            pass
        return (content,)
