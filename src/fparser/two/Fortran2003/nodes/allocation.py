from allocate_object import Allocate_Object
from allocate_shape_spec import Allocate_Shape_Spec_List

class Allocation(CallBase):  # R628
    """
    ::

        <allocation> = <allocate-object> [ ( <allocate-shape-spec-list> ) ]
                     | <variable-name>

    """

    subclass_names = ["Variable_Name", "Allocate_Object"]
    use_names = ["Allocate_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Allocate_Object, Allocate_Shape_Spec_List, string, require_rhs=True
        )


class Allocation_List(SequenceBase):
    subclass_names = ["Allocation"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Allocation, string)

    def __iter__(self):
        return iter(self.items)
