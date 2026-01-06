class Forall_Stmt(StmtBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R759::

        forall-stmt is FORALL forall-header forall-assignment-stmt

    """

    subclass_names = []
    use_names = ["Forall_Header", "Forall_Assignment_Stmt"]

    @staticmethod
    def match(string):
        """Implements the matching for a forall statement.

        :param string: A string or the fortran reader containing the \
                    line of code that we are trying to match.
        :type string: `str` or \
        :py:class:`fparser.common.readfortran.FortranReader`
        :return: `None` if there is no match or a `tuple` of size 2 \
        containing an instance of the Forall_Header class followed by \
        an instance of the Forall_Assignment_Stmt class.
        :rtype: `None` or ( \
        :py:class:`fparser.two.Fortran2003.Forall_Header`, \
        :py:class:`fparser.two.Fortran2003.Forall_Assignment_Stmt`)

        """
        strip_string = string.strip()
        if strip_string[:6].upper() != "FORALL":
            return None
        line, repmap = string_replace_map(strip_string[6:].lstrip())
        if not line.startswith("("):
            return None
        index = line.find(")")
        if index == -1:
            return None
        header = repmap(line[: index + 1])
        # No need to check if header variable is empty as we know it
        # will contain brackets at least
        line = repmap(line[index + 1 :].lstrip())
        if not line:
            return None
        return Forall_Header(header), Forall_Assignment_Stmt(line)

    def tostr(self):
        """
        :return: this forall statement as a string
        :rtype: str
        :raises InternalError: if the internal items list variable is \
        not the expected size.
        :raises InternalError: if the first element of the internal \
        items list is None or is an empty string.
        :raises InternalError: if the second element of the internal \
        items list is None or is an empty string.
        """
        if len(self.items) != 2:
            raise InternalError(
                "Class Forall_Stmt method tostr() has '{0}' items, "
                "but expecting 2.".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "Class Forall_Stmt method tostr(). 'Items' entry 0 "
                "should be a valid Forall_Header."
            )
        if not self.items[1]:
            raise InternalError(
                "Class Forall_Stmt method tostr(). 'Items' entry 1 should "
                "be a valid Forall_Assignment_Stmt"
            )
        return "FORALL {0} {1}".format(self.items[0], self.items[1])
