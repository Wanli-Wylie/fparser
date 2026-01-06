from fparser.two.utils import (
    SeparatorBase,
    SequenceBase,
)

from lower_bound import Lower_Bound

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


class Assumed_Shape_Spec_List(SequenceBase):
    subclass_names = ["Assumed_Shape_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Assumed_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)
