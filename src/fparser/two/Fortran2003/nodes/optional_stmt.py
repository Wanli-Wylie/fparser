from fparser.two.utils import (
    WORDClsBase,
    StmtBase,
)

from dummy_arg_name import Dummy_Arg_Name_List

class Optional_Stmt(StmtBase, WORDClsBase):  # R537
    """
    ::

        <optional-stmt> = OPTIONAL [ :: ] <dummy-arg-name-list>

    """

    subclass_names = []
    use_names = ["Dummy_Arg_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "OPTIONAL", Dummy_Arg_Name_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
