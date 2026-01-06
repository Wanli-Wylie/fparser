from data_ref import Data_Ref
from name import Binding_Name

class Procedure_Designator(BinaryOpBase):  # R1219
    """
    ::

        <procedure-designator> = <procedure-name>
                                 | <proc-component-ref>
                                 | <data-ref> % <binding-name>

    """

    subclass_names = ["Procedure_Name", "Proc_Component_Ref"]
    use_names = ["Data_Ref", "Binding_Name"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Data_Ref, pattern.percent_op.named(), Binding_Name, string
        )
