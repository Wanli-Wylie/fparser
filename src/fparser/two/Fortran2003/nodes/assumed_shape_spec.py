class Assumed_Shape_Spec(SeparatorBase):  # R514
    """
    Fortran2003 Rule R514::

        <assumed-shape-spec> = [ <lower-bound> ] :

    """

    subclass_names = []
    use_names = ["Lower_Bound"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Lower_Bound, None, string)
