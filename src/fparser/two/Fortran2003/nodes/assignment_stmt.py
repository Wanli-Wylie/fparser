class Assignment_Stmt(StmtBase, BinaryOpBase):  # R734
    """
    ::

        <assignment-stmt> = <variable> = <expr>

    """

    subclass_names = []
    use_names = ["Variable", "Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Variable, "=", Expr, string, right=False)
