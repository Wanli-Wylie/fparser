from fparser.two.utils import (
    WORDClsBase,
    StmtBase,
)

from pointer_decl import Pointer_Decl_List

class Pointer_Stmt(StmtBase, WORDClsBase):  # R540
    """
    ::

        <pointer-stmt> = POINTER [ :: ] <pointer-decl-list>

    """

    subclass_names = []
    use_names = ["Pointer_Decl_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "POINTER", Pointer_Decl_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
