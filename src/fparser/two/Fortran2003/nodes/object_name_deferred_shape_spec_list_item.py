from fparser.two.utils import (
    CallBase,
    SequenceBase,
)

from deferred_shape_spec import Deferred_Shape_Spec_List
from object_name import Object_Name

class Object_Name_Deferred_Shape_Spec_List_Item(CallBase):
    """
    ::

        <..> =  <object-name> [ ( <deferred-shape-spec-list> ) ]

    """

    subclass_names = ["Object_Name"]
    use_names = ["Deferred_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Object_Name, Deferred_Shape_Spec_List, string, require_rhs=True
        )


class Object_Name_Deferred_Shape_Spec_List_Item_List(SequenceBase):
    subclass_names = ["Object_Name_Deferred_Shape_Spec_List_Item"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(
            r",", Object_Name_Deferred_Shape_Spec_List_Item, string
        )

    def __iter__(self):
        return iter(self.items)
