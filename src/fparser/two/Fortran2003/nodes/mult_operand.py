class Mult_Operand(BinaryOpBase):  # R704
    """
    ::

        <mult-operand> = <level-1-expr> [ <power-op> <mult-operand> ]
        <power-op> = **

    """

    subclass_names = ["Level_1_Expr"]
    use_names = ["Mult_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_1_Expr, pattern.power_op.named(), Mult_Operand, string, right=False
        )
