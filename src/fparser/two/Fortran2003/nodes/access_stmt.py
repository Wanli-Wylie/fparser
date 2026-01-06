from fparser.two.utils import (
    WORDClsBase,
    StmtBase,
)

from access_id import Access_Id_List

class Access_Stmt(StmtBase, WORDClsBase):  # R518
    """
    Fortran2003 Rule R518::

        <access-stmt> = <access-spec> [ [ :: ] <access-id-list> ]

    """

    subclass_names = []
    use_names = ["Access_Spec", "Access_Id_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            ["PUBLIC", "PRIVATE"],
            Access_Id_List,
            string,
            colons=True,
            require_cls=False,
        )

    tostr = WORDClsBase.tostr_a
