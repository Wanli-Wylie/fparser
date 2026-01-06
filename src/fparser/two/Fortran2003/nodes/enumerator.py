class Enumerator(BinaryOpBase):  # R463
    """
    ::

        <enumerator> = <named-constant> [ = <scalar-int-initialization-expr> ]

    """

    subclass_names = ["Named_Constant"]
    use_names = ["Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string):
        if "=" not in string:
            return
        lhs, rhs = string.split("=", 1)
        return (
            Named_Constant(lhs.rstrip()),
            "=",
            Scalar_Int_Initialization_Expr(rhs.lstrip()),
        )


class Enumerator_List(SequenceBase):
    subclass_names = ["Enumerator"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Enumerator, string)

    def __iter__(self):
        return iter(self.items)
