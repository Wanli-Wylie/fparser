from name import Associate_Construct_Name

class End_Associate_Stmt(EndStmtBase):  # R820
    """
    <end-associate-stmt> = END ASSOCIATE [ <associate-construct-name> ]
    """

    subclass_names = []
    use_names = ["Associate_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "ASSOCIATE", Associate_Construct_Name, string, require_stmt_type=True
        )
