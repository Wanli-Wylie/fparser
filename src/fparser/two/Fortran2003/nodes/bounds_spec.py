class Bounds_Spec(SeparatorBase):  # R737
    """
    ::

        <bounds-spec> = <lower-bound-expr> :

    """

    subclass_names = []
    use_names = ["Lower_Bound_Expr"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Lower_Bound_Expr, None, string, require_lhs=True)


class Bounds_Spec_List(SequenceBase):
    subclass_names = ["Bounds_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Bounds_Spec, string)

    def __iter__(self):
        return iter(self.items)
