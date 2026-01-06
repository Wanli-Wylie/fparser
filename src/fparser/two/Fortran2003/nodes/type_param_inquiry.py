from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    BinaryOpBase,
)

from designator import Designator
from name import Type_Param_Name

class Type_Param_Inquiry(BinaryOpBase):  # R615
    """
    ::

        <type-param-inquiry> = <designator> % <type-param-name>

    """

    subclass_names = []
    use_names = ["Designator", "Type_Param_Name"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Designator, pattern.percent_op.named(), Type_Param_Name, string
        )
