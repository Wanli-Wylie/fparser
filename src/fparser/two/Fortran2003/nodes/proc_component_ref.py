from fparser.two.utils import (
    BinaryOpBase,
)

from name import Procedure_Component_Name
from variable import Variable

class Proc_Component_Ref(BinaryOpBase):  # R741
    """
    ::

        <proc-component-ref> = <variable> % <procedure-component-name>

    """

    subclass_names = []
    use_names = ["Variable", "Procedure_Component_Name"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Variable, r"%", Procedure_Component_Name, string)
