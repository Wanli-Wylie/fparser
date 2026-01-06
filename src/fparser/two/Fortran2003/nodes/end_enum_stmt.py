from fparser.two.utils import (
    EndStmtBase,
)

class End_Enum_Stmt(EndStmtBase):  # R464
    """
    ::

        <end-enum-stmt> = END ENUM

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return EndStmtBase.match("ENUM", None, string, require_stmt_type=True)
