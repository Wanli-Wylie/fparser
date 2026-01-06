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
