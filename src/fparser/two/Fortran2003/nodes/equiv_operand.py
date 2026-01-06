class Equiv_Operand(BinaryOpBase):  # R716
    """
    ::

        <equiv-operand> = [ <equiv-operand> <or-op> ] <or-operand>
        <or-op>  = .OR.

    """

    subclass_names = ["Or_Operand"]
    use_names = ["Equiv_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Equiv_Operand, pattern.or_op.named(), Or_Operand, string
        )
