from name import Case_Construct_Name

class End_Select_Stmt(EndStmtBase):  # R811
    """
    <end-select-stmt> = END SELECT [ <case-construct-name> ]
    """

    subclass_names = []
    use_names = ["Case_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "SELECT", Case_Construct_Name, string, require_stmt_type=True
        )
