class Substring_Range(SeparatorBase):  # R611
    """
    ::

        <substring-range> = [ <scalar-int-expr> ] : [ <scalar-int-expr> ]

    """

    subclass_names = []
    use_names = ["Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Scalar_Int_Expr, Scalar_Int_Expr, string)
