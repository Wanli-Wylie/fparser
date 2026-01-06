from explicit_shape_spec import Explicit_Shape_Spec_List
from variable_name import Variable_Name

class Common_Block_Object(CallBase):  # R558
    """
    ::

        <common-block-object> = <variable-name> [ ( <explicit-shape-spec-list> ) ]
                                | <proc-pointer-name>

    """

    subclass_names = ["Proc_Pointer_Name", "Variable_Name"]
    use_names = ["Variable_Name", "Explicit_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Variable_Name, Explicit_Shape_Spec_List, string, require_rhs=True
        )


class Common_Block_Object_List(SequenceBase):
    subclass_names = ["Common_Block_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Common_Block_Object, string)

    def __iter__(self):
        return iter(self.items)
