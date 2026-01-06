class Explicit_Shape_Spec(SeparatorBase):  # R511
    """
    ::

        <explicit-shape-spec> = [ <lower-bound> : ] <upper-bound>

    """

    subclass_names = []
    use_names = ["Lower_Bound", "Upper_Bound"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        if ":" not in line:
            return None, Upper_Bound(string)
        lower, upper = line.split(":", 1)
        lower = lower.rstrip()
        upper = upper.lstrip()
        if not upper:
            return
        if not lower:
            return
        return Lower_Bound(repmap(lower)), Upper_Bound(repmap(upper))

    def tostr(self):
        if self.items[0] is None:
            return str(self.items[1])
        return SeparatorBase.tostr(self)


class Explicit_Shape_Spec_List(SequenceBase):
    subclass_names = ["Explicit_Shape_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Explicit_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)
