class Binding_Private_Stmt(StmtBase, STRINGBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R449::

        <binding-private-stmt> = PRIVATE

    For binding private statement within the type-bound procedure
    part of a derived type.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match

        :return: keyword  "PRIVATE" or None if no match is found
        :rtype: str or None
        """
        return StringBase.match("PRIVATE", string.upper())
