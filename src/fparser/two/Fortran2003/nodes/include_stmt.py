from include_filename import Include_Filename

class Include_Stmt(Base):  # pylint: disable=invalid-name
    """Implements the matching of a Fortran include statement. There is no
    rule for this as the compiler is expected to inline any content
    from an include statement when one is found. However, for a parser
    it can make sense to represent an include statement in a parse
    tree::

        include-stmt is INCLUDE ['filename' or "filename"]

    """

    use_names = ["Include_Filename"]

    @staticmethod
    def match(string):
        """Implements the matching for an include statement.

        :param str string: the string to match with as an include statement.
        :returns: a tuple of size 1 containing an Include_Filename \
        object with the matched filename if there is a match, or None \
        if there is not.
        :rtype: (:py:class:`fparser.two.Fortran2003.Include_Filename`) \
        or NoneType

        """
        if not string:
            return None

        line = string.strip()
        if line[:7].upper() != "INCLUDE":
            # The line does not start with the include token and/or the line
            # is too short.
            return None
        rhs = line[7:].strip()
        if rhs is None or len(rhs) < 3:
            # Either we didn't find any includes or the content after
            # the include token is too short to be valid (it must at
            # least contain quotes and one character.
            return None
        if not (
            (rhs[0] == "'" and rhs[-1] == "'") or (rhs[0] == '"' and rhs[-1] == '"')
        ):
            # The filename should be surrounded by single or double
            # quotes but this is not the case.
            return None
        # Remove the quotes.
        file_name = rhs[1:-1]
        # Pass the potential filename to the relevant class.
        name = Include_Filename(file_name)
        if not name:
            raise InternalError(
                "Fortran2003.py:Include_Stmt:match Include_Filename should "
                "never return None or an empty name"
            )
        return (name,)

    def tostr(self):
        """
        :return: this include_stmt as a string
        :rtype: str
        """

        return "INCLUDE '{0}'".format(self.items[0])
