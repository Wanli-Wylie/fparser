class Deferred_Shape_Spec(SeparatorBase):  # R515
    """
    Fortran2003 Rule R515::

        <deferred_shape_spec> = :

    """

    subclass_names = []

    @staticmethod
    def match(string):
        if string == ":":
            return None, None
        return None


class Deferred_Shape_Spec_List(SequenceBase):
    subclass_names = ["Deferred_Shape_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Deferred_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)
