from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)

from explicit_shape_spec import Explicit_Shape_Spec_List
from lower_bound import Lower_Bound

class Assumed_Size_Spec(Base):  # R516
    """
    Fortran2003 Rule R516::

        <assumed-size-spec> = [ <explicit-shape-spec-list> , ]
            [ <lower-bound> : ] *

    """

    subclass_names = []
    use_names = ["Explicit_Shape_Spec_List", "Lower_Bound"]

    @staticmethod
    def match(string):
        if not string.endswith("*"):
            return
        line = string[:-1].rstrip()
        if not line:
            return None, None
        if line.endswith(":"):
            line, repmap = string_replace_map(line[:-1].rstrip())
            i = line.rfind(",")
            if i == -1:
                return None, Lower_Bound(repmap(line))
            return (
                Explicit_Shape_Spec_List(repmap(line[:i].rstrip())),
                Lower_Bound(repmap(line[i + 1 :].lstrip())),
            )
        if not line.endswith(","):
            return
        line = line[:-1].rstrip()
        return Explicit_Shape_Spec_List(line), None

    def tostr(self):
        s = ""
        if self.items[0] is not None:
            s += str(self.items[0]) + ", "
        if self.items[1] is not None:
            s += str(self.items[1]) + " : "
        s += "*"
        return s
