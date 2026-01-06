class Directive(Base):
    """
    Represents a Directive. Directives are leaves in the tree, containing
    a single item consisting of the directive string.

    Fparser supports the following directive formats:

        1. '!$', 'c$' or '*$' followed by any alphabetical character for
           generic directives.
        2. '!dir$' or 'cdir$' for the flang, ifx or ifort compilers.
        3. '!gcc$' for the gfortran compiler.
    """

    subclass_names = []
    _directive_formats = [
        r"\!\$[a-z]",  # Generic directive
        r"c\$[a-z]",  # Generic directive
        r"\*\$[a-z]",  # Generic directive
        r"\!dir\$",  # flang, ifx, ifort directives.
        r"cdir\$",  # flang, ifx, ifort fixed format directive.
        r"\!gcc\$",  # GCC compiler directive
    ]

    @show_result
    def __new__(cls, string: Union[str, FortranReaderBase], parent_cls=None):
        """
        Create a new Directive instance.

        :param type cls: the class of object to create.
        :param string: (source of) Fortran string to parse.
        :param parent_cls: the parent class of this object.
        :type parent_cls: :py:type:`type`

        """
        from fparser.common import readfortran

        if isinstance(string, readfortran.Comment):
            # Inline comments cannot be directives.
            if string.inline:
                return
            # Directives must start with one of the specified directive
            # prefixes.
            lower = string.comment.lower()
            if not (
                any(
                    [
                        re.match(prefix, lower) is not None
                        for prefix in Directive._directive_formats
                    ]
                )
            ):
                return
            # We were after a directive and we got a directive. Construct
            # one manually to avoid recursively calling this __new__
            # method again...
            obj = object.__new__(cls)
            obj.init(string)
            return obj
        if isinstance(string, FortranReaderBase):
            reader = string
            item = reader.get_item()
            if item is None:
                return
            if isinstance(item, readfortran.Comment):
                # This effectively recursively calls this routine
                res = Directive(item)
                if not res:
                    # We didn't get a directive so put the item back in
                    # the FIFO
                    reader.put_item(item)
                return res
            # We didn't get a directive so put the item back in the FIFO
            reader.put_item(item)
        # We didn't get a directive
        return

    def init(self, comment) -> None:
        """
        Initialise this Directive from a comment object.

        :param comment: The comment object produced by the reader
        :type comment: :py:class:`readfortran.Comment`
        """
        self.items = [comment.comment]
        self.item = comment

    def tostr(self) -> str:
        """
        :returns: this directive as a string.
        """
        return str(self.items[0])
