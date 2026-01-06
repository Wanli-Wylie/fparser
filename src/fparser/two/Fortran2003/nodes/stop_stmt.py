from stop_code import Stop_Code

class Stop_Stmt(StmtBase, WORDClsBase):  # R849
    """
    <stop-stmt> = STOP [ <stop-code> ]
    """

    subclass_names = []
    use_names = ["Stop_Code"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("STOP", Stop_Code, string)
