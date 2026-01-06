from action_stmt import Action_Stmt

class Action_Stmt_C802(Base):
    """
    ::

        <action-stmt-c802> = <action-stmt>

    C802 is applied.

    """

    subclass_names = Action_Stmt.subclass_names[:]
    subclass_names.remove("End_Function_Stmt")
    subclass_names.remove("End_Subroutine_Stmt")
    subclass_names.remove("If_Stmt")
