from fparser.two.utils import (
    CallBase,
)

from parent_string import Parent_String
from substring_range import Substring_Range

class Substring(CallBase):  # R609
    """
    ::

        <substring> = <parent-string> ( <substring-range> )

    """

    subclass_names = []
    use_names = ["Parent_String", "Substring_Range"]

    @staticmethod
    def match(string):
        return CallBase.match(Parent_String, Substring_Range, string, require_rhs=True)
