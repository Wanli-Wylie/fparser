from fparser.two.utils import (
    BinaryOpBase,
    SequenceBase,
)

from name import Procedure_Entity_Name
from null_init import Null_Init

class Proc_Decl(BinaryOpBase):  # R1214
    """
    ::

        <proc-decl> = <procedure-entity-name> [ => <null-init> ]

    Attributes::

        items : (Procedure_Entity_Name, Null_Init)

    """

    subclass_names = ["Procedure_Entity_Name"]
    use_names = ["Null_Init"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Procedure_Entity_Name, "=>", Null_Init, string)


class Proc_Decl_List(SequenceBase):
    subclass_names = ["Proc_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Proc_Decl, string)

    def __iter__(self):
        return iter(self.items)
