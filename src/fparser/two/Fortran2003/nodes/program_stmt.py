from name import Program_Name

class Program_Stmt(StmtBase, WORDClsBase, ScopingRegionMixin):  # R1102
    """
    Fortran 2003 rule R1102::

        program-stmt is PROGRAM program-name

    """

    subclass_names = []
    use_names = ["Program_Name"]

    @staticmethod
    def match(string):
        """Implements the matching for a Program Statement. Makes use of
        `WORDClsBase`, as the required match is a string followed by a
        class. The class is made compulsory for the match as the
        PROGRAM keyword is not valid without a program name.

        :param str string: Fortran code to check for a match
        :returns: `None` if there is no match or, if there is a match, \
                  a tuple of size 2 with the first entry being the \
                  string 'PROGRAM' and the second entry being a `Name` \
                  class containing the name of the program.
        :rtype: `NoneType` or ( `str`, \
                :py:class:`fparser.two.Fortran2003.Name` )

        """
        return WORDClsBase.match("PROGRAM", Program_Name, string, require_cls=True)

    def get_name(self):
        """Provides the program name as an instance of the `Name` class.

        :returns: the program name as a :py:class:`Name` class
        :rtype: :py:class:`Name`

        """
        return self.items[1]

    def get_start_name(self):
        """Provides the program name as a string. This is used for matching
        with the equivalent `end program` name if there is one.

        :returns: the program name as a string
        :rtype: str

        """
        return self.get_name().string
