from fparser.two.utils import (
    CALLBase,
)

from component_array_spec import Component_Array_Spec

class Dimension_Component_Attr_Spec(CALLBase):
    """
    ::

        <dimension-component-attr-spec> = DIMENSION ( <component-array-spec> )

    """

    subclass_names = []
    use_names = ["Component_Array_Spec"]

    @staticmethod
    def match(string):
        return CALLBase.match("DIMENSION", Component_Array_Spec, string)
