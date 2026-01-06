from fparser.two.utils import (
    BinaryOpBase,
)

from name import Data_Pointer_Component_Name
from variable import Variable

class Data_Pointer_Object(BinaryOpBase):  # R736
    """
    ::

        <data-pointer-object> = <variable-name>
                                | <variable> % <data-pointer-component-name>

    """

    subclass_names = ["Variable_Name"]
    use_names = ["Variable", "Data_Pointer_Component_Name"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Variable, r"%", Data_Pointer_Component_Name, string)
