class End_Type_Stmt(EndStmtBase):  # R433
    """
    ::

        <end-type-stmt> = END TYPE [ <type-name> ]

    """

    subclass_names = []
    use_names = ["Type_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("TYPE", Type_Name, string, require_stmt_type=True)
