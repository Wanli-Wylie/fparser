from fparser.two.utils import (
    CallBase,
)

from actual_arg_spec import Actual_Arg_Spec_List
from procedure_designator import Procedure_Designator

class Function_Reference(CallBase):  # R1217
    """
    <function-reference> = <procedure-designator>
        ( [ <actual-arg-spec-list> ] )
    """

    subclass_names = []
    use_names = ["Procedure_Designator", "Actual_Arg_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(Procedure_Designator, Actual_Arg_Spec_List, string)
