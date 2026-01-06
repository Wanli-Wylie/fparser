from name import Where_Construct_Name

class End_Where_Stmt(EndStmtBase):  # R751
    """
    <end-where-stmt> = END WHERE [ <where-construct-name> ]
    """

    subclass_names = []
    use_names = ["Where_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "WHERE", Where_Construct_Name, string, require_stmt_type=True
        )
