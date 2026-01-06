from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
    SequenceBase,
)

from name import Index_Name
from stride import Stride
from subscript import Subscript

class Forall_Triplet_Spec(Base):  # R755
    """
    ::

        <forall-triplet-spec> = <index-name> = <subscript> :
            <subscript> [ : <stride> ]

    """

    subclass_names = []
    use_names = ["Index_Name", "Subscript", "Stride"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        i = line.find("=")
        if i == -1:
            return
        n = Index_Name(repmap(line[:i].rstrip()))
        line = line[i + 1 :].lstrip()
        s = [repmap(s.strip()) for s in line.split(":")]
        if len(s) == 2:
            return n, Subscript(s[0]), Subscript(s[1]), None
        if len(s) == 3:
            return n, Subscript(s[0]), Subscript(s[1]), Stride(s[2])

    def tostr(self):
        if self.items[3] is None:
            return "%s = %s : %s" % (self.items[:3])
        return "%s = %s : %s : %s" % (self.items)


class Forall_Triplet_Spec_List(SequenceBase):
    subclass_names = ["Forall_Triplet_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Forall_Triplet_Spec, string)

    def __iter__(self):
        return iter(self.items)
