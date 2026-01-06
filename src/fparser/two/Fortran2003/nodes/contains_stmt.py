from fparser.two.utils import (
    STRINGBase,
    StmtBase,
)

class Contains_Stmt(StmtBase, STRINGBase):  # R1237
    """
    <contains-stmt> = CONTAINS
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match("CONTAINS", string)
