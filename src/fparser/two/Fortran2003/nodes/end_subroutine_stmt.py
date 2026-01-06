from fparser.two.utils import (
    EndStmtBase,
)

from name import Subroutine_Name

class End_Subroutine_Stmt(EndStmtBase):  # R1234
    """
    <end-subroutine-stmt> = END [ SUBROUTINE [ <subroutine-name> ] ]
    """

    subclass_names = []
    use_names = ["Subroutine_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("SUBROUTINE", Subroutine_Name, string)
