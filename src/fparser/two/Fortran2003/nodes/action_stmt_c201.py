from fparser.two.utils import (
    Base,
)

from action_stmt import Action_Stmt

class Action_Stmt_C201(Base):
    """
    ::

        <action-stmt-c201> = <action-stmt>

    C201 is applied.

    """

    subclass_names = Action_Stmt.subclass_names[:]
    subclass_names.remove("End_Function_Stmt")
    subclass_names.remove("End_Subroutine_Stmt")
