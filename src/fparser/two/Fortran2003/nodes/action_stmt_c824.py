class Action_Stmt_C824(Base):
    """
    ::

        <action-stmt-c824> = <action-stmt>

    C824 is applied.
    """

    subclass_names = Action_Stmt.subclass_names[:]
    subclass_names.remove("End_Function_Stmt")
    subclass_names.remove("End_Subroutine_Stmt")
    subclass_names.remove("Continue_Stmt")
    subclass_names.remove("Goto_Stmt")
    subclass_names.remove("Return_Stmt")
    subclass_names.remove("Stop_Stmt")
    subclass_names.remove("Exit_Stmt")
    subclass_names.remove("Cycle_Stmt")
    subclass_names.remove("Arithmetic_If_Stmt")
