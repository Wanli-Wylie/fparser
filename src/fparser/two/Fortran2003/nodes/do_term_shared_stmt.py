from fparser.two.utils import (
    StmtBase,
)

class Do_Term_Shared_Stmt(StmtBase):  # R842
    """
    ::

        <do-term-shared-stmt> = <action-stmt>

    C826 - see C824 above.
    """

    subclass_names = ["Action_Stmt"]
