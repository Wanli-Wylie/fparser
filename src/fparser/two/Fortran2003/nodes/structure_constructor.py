from fparser.two.utils import (
    CallBase,
)

from component_spec import Component_Spec_List
from derived_type_spec import Derived_Type_Spec

class Structure_Constructor(CallBase):  # R457
    """
    ::

        <structure-constructor> = <derived-type-spec> ( [ <component-spec-list> ] )

    """

    subclass_names = []
    use_names = ["Derived_Type_Spec", "Component_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(Derived_Type_Spec, Component_Spec_List, string)
