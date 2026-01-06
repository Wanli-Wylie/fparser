class Return_Stmt(StmtBase):  # R1236
    """
    <return-stmt> = RETURN [ <scalar-int-expr> ]
    """

    subclass_names = []
    use_names = ["Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        start = string[:6].upper()
        if start != "RETURN":
            return
        if len(string) == 6:
            return (None,)
        return (Scalar_Int_Expr(string[6:].lstrip()),)

    def tostr(self):
        if self.items[0] is None:
            return "RETURN"
        return "RETURN %s" % self.items
