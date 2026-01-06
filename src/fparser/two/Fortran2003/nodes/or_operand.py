class Or_Operand(BinaryOpBase):  # R715
    """
    ::

        <or-operand> = [ <or-operand> <and-op> ] <and-operand>
        <and-op> = .AND.

    """

    subclass_names = ["And_Operand"]
    use_names = ["Or_Operand", "And_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Or_Operand, pattern.and_op.named(), And_Operand, string
        )
