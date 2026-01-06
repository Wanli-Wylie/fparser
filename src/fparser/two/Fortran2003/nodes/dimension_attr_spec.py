from fparser.two.utils import (
    CALLBase,
)

from array_spec import Array_Spec

class Dimension_Attr_Spec(CALLBase):  # R503.d
    """
    ::

        <dimension-attr-spec> = DIMENSION ( <array-spec> )

    """

    subclass_names = []
    use_names = ["Array_Spec"]

    @staticmethod
    def match(string):
        return CALLBase.match("DIMENSION", Array_Spec, string)
