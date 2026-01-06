from level_2_expr import Level_2_Expr

class Level_3_Expr(BinaryOpBase):  # R710
    """
    ::

        <level-3-expr> = [ <level-3-expr> <concat-op> ] <level-2-expr>
        <concat-op>    = //

    """

    subclass_names = ["Level_2_Expr"]
    use_names = ["Level_3_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_3_Expr, pattern.concat_op.named(), Level_2_Expr, string
        )
