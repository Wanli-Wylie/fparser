from fparser.two.utils import (
    WORDClsBase,
    StmtBase,
)

from name import Do_Construct_Name

class Cycle_Stmt(StmtBase, WORDClsBase):  # R843
    """
    <cycle-stmt> = CYCLE [ <do-construct-name> ]
    """

    subclass_names = []
    use_names = ["Do_Construct_Name"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("CYCLE", Do_Construct_Name, string)
