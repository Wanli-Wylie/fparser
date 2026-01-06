class Exit_Stmt(StmtBase, WORDClsBase):  # R844
    """
    <exit-stmt> = EXIT [ <do-construct-name> ]
    """

    subclass_names = []
    use_names = ["Do_Construct_Name"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("EXIT", Do_Construct_Name, string)
