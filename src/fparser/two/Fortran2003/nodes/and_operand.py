class And_Operand(UnaryOpBase):  # R714
    """
    ::

        <and-operand> = [ <not-op> ] <level-4-expr>
        <not-op> = .NOT.

    """

    subclass_names = ["Level_4_Expr"]
    use_names = []

    @staticmethod
    def match(string):
        return UnaryOpBase.match(pattern.not_op.named(), Level_4_Expr, string)
