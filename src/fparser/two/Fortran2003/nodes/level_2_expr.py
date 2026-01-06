from add_operand import Add_Operand

class Level_2_Expr(BinaryOpBase):  # R706
    """
    ::

        <level-2-expr> = [ [ <level-2-expr> ] <add-op> ] <add-operand>
        <level-2-expr> = [ <level-2-expr> <add-op> ] <add-operand>
                         | <level-2-unary-expr>
        <add-op>   = +
                     | -

    """

    subclass_names = ["Level_2_Unary_Expr"]
    use_names = ["Level_2_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_2_Expr, pattern.add_op.named(), Add_Operand, string
        )
