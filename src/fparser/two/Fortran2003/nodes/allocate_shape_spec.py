from lower_bound_expr import Lower_Bound_Expr
from upper_bound_expr import Upper_Bound_Expr

class Allocate_Shape_Spec(SeparatorBase):  # R630
    """
    ::

        <allocate-shape-spec> = [ <lower-bound-expr> : ] <upper-bound-expr>

    """

    subclass_names = []
    use_names = ["Lower_Bound_Expr", "Upper_Bound_Expr"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        if ":" not in line:
            return None, Upper_Bound_Expr(string)
        lower, upper = line.split(":", 1)
        lower = lower.rstrip()
        upper = upper.lstrip()
        if not upper:
            return
        if not lower:
            return
        return Lower_Bound_Expr(repmap(lower)), Upper_Bound_Expr(repmap(upper))

    def tostr(self):
        if self.items[0] is None:
            return str(self.items[1])
        return SeparatorBase.tostr(self)


class Allocate_Shape_Spec_List(SequenceBase):
    subclass_names = ["Allocate_Shape_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Allocate_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)
