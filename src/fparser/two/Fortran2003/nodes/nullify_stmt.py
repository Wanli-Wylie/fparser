from fparser.two.utils import (
    StmtBase,
    CALLBase,
)

from pointer_object import Pointer_Object_List

class Nullify_Stmt(StmtBase, CALLBase):  # R633
    """
    ::

        <nullify-stmt> = NULLIFY ( <pointer-object-list> )

    """

    subclass_names = []
    use_names = ["Pointer_Object_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("NULLIFY", Pointer_Object_List, string, require_rhs=True)
