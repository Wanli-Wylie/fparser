from fparser.two.utils import (
    WORDClsBase,
    StmtBase,
)

from enumerator import Enumerator_List

class Enumerator_Def_Stmt(StmtBase, WORDClsBase):  # R462
    """
    ::

        <enumerator-def-stmt> = ENUMERATOR [ :: ] <enumerator-list>

    """

    subclass_names = []
    use_names = ["Enumerator_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "ENUMERATOR", Enumerator_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
