class End_Select_Type_Stmt(EndStmtBase):  # R824
    """
    <end-select-type-stmt> = END SELECT [ <select-construct-name> ]
    """

    subclass_names = []
    use_names = ["Select_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "SELECT", Select_Construct_Name, string, require_stmt_type=True
        )
