class End_Do_Stmt(EndStmtBase):  # pylint: disable=invalid-name
    """
    R834::

        <end-do-stmt> = END DO [ <do-construct-name> ]

    """

    subclass_names = []
    use_names = ["Do_Construct_Name"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: code line matching the "END DO" statement
        :rtype: string
        """
        return EndStmtBase.match(
            "DO", Do_Construct_Name, string, require_stmt_type=True
        )
