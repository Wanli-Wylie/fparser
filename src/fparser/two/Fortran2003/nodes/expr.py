from level_5_expr import Level_5_Expr

class Expr(BinaryOpBase):  # R722
    """
    ::

        <expr> = [ <expr> <defined-binary-op> ] <level-5-expr>
        <defined-binary-op> = . <letter> [ <letter> ]... .

    """

    subclass_names = ["Level_5_Expr"]
    use_names = ["Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Expr,
            pattern.defined_binary_op.named(),
            Level_5_Expr,
            string,
            exclude_op_pattern=pattern.non_defined_binary_op,
        )


class Scalar_Expr(Base):
    subclass_names = ["Expr"]
