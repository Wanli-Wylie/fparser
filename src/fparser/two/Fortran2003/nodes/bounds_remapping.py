class Bounds_Remapping(SeparatorBase):  # R738
    """
    ::

        <bounds-remapping> = <lower-bound-expr> : <upper-bound-expr>

    """

    subclass_names = []
    use_classes = ["Lower_Bound_Expr", "Upper_Bound_Expr"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(
            Lower_Bound_Expr,
            Upper_Bound_Expr,
            string,
            require_lhs=True,
            require_rhs=True,
        )
