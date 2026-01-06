class End_If_Stmt(EndStmtBase):  # R806
    """
    <end-if-stmt> = END IF [ <if-construct-name> ]
    """

    subclass_names = []
    use_names = ["If_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "IF", If_Construct_Name, string, require_stmt_type=True
        )
