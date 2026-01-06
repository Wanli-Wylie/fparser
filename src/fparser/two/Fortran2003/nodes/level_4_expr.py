class Level_4_Expr(BinaryOpBase):  # R712
    """
    ::

        <level-4-expr> = [ <level-3-expr> <rel-op> ] <level-3-expr>
        <rel-op> = .EQ. | .NE. | .LT. | .LE. | .GT. | .GE. | == |
            /= | < | <= | > | >=

    """

    subclass_names = ["Level_3_Expr"]
    use_names = []

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_3_Expr, pattern.rel_op.named(), Level_3_Expr, string
        )
