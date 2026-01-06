class Association(BinaryOpBase):  # R818
    """
    <association> = <associate-name> => <selector>
    """

    subclass_names = []
    use_names = ["Associate_Name", "Selector"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Associate_Name, "=>", Selector, string)
