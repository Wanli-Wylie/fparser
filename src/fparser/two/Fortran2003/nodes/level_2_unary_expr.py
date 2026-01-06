class Level_2_Unary_Expr(UnaryOpBase):  # R706.c
    """
    ::

        <level-2-unary-expr> = [ <add-op> ] <add-operand>

    """

    subclass_names = ["Add_Operand"]
    use_names = []

    @staticmethod
    def match(string):
        return UnaryOpBase.match(pattern.add_op.named(), Add_Operand, string)
