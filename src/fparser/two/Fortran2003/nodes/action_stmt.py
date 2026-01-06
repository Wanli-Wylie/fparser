from fparser.two.utils import (
    Base,
)

class Action_Stmt(Base):  # R214
    """
    ::

        <action-stmt> = <allocate-stmt>
                        | <assignment-stmt>
                        | <backspace-stmt>
                        | <call-stmt>
                        | <close-stmt>
                        | <continue-stmt>
                        | <cycle-stmt>
                        | <deallocate-stmt>
                        | <endfile-stmt>
                        | <end-function-stmt>
                        | <end-program-stmt>
                        | <end-subroutine-stmt>
                        | <exit-stmt>
                        | <flush-stmt>
                        | <forall-stmt>
                        | <goto-stmt>
                        | <if-stmt>
                        | <inquire-stmt>
                        | <nullify-stmt>
                        | <open-stmt>
                        | <pointer-assignment-stmt>
                        | <print-stmt>
                        | <read-stmt>
                        | <return-stmt>
                        | <rewind-stmt>
                        | <stop-stmt>
                        | <wait-stmt>
                        | <where-stmt>
                        | <write-stmt>
                        | <arithmetic-if-stmt>
                        | <computed-goto-stmt>

    """

    subclass_names = [
        "Allocate_Stmt",
        "Assignment_Stmt",
        "Backspace_Stmt",
        "Call_Stmt",
        "Close_Stmt",
        "Comment",
        "Continue_Stmt",
        "Cycle_Stmt",
        "Deallocate_Stmt",
        "Endfile_Stmt",
        "End_Function_Stmt",
        "End_Subroutine_Stmt",
        "Exit_Stmt",
        "Flush_Stmt",
        "Forall_Stmt",
        "Goto_Stmt",
        "If_Stmt",
        "Inquire_Stmt",
        "Nullify_Stmt",
        "Open_Stmt",
        "Pointer_Assignment_Stmt",
        "Print_Stmt",
        "Read_Stmt",
        "Return_Stmt",
        "Rewind_Stmt",
        "Stop_Stmt",
        "Wait_Stmt",
        "Where_Stmt",
        "Write_Stmt",
        "Arithmetic_If_Stmt",
        "Computed_Goto_Stmt",
    ]
