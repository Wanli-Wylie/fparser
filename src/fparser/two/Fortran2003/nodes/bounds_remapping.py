from lower_bound_expr import Lower_Bound_Expr
from upper_bound_expr import Upper_Bound_Expr

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


class Bounds_Remapping_List(SequenceBase):
    subclass_names = ["Bounds_Remapping"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Bounds_Remapping, string)

    def __iter__(self):
        return iter(self.items)
