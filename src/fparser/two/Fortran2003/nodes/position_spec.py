from fparser.two.utils import (
    KeywordValueBase,
    SequenceBase,
)
from fparser.two.utils import (
    NoMatchError,
)

from file_unit_number import File_Unit_Number
from int_variable import Scalar_Int_Variable
from iomsg_variable import Iomsg_Variable
from label import Label

class Position_Spec(KeywordValueBase):  # R926
    """
    ::

        <position-spec> = [ UNIT = ] <file-unit-number>
                          | IOMSG = <iomsg-variable>
                          | IOSTAT = <scalar-int-variable>
                          | ERR = <label>

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Iomsg_Variable", "Scalar_Int_Variable", "Label"]

    @staticmethod
    def match(string):
        for k, v in [
            ("ERR", Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)


class Position_Spec_List(SequenceBase):
    subclass_names = ["Position_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Position_Spec, string)

    def __iter__(self):
        return iter(self.items)
