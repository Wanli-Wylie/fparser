class Specification_Stmt(Base):  # R212
    """
    ::

        <specification-stmt> = <access-stmt>
                               | <allocatable-stmt>
                               | <asynchronous-stmt>
                               | <bind-stmt>
                               | <common-stmt>
                               | <data-stmt>
                               | <dimension-stmt>
                               | <equivalence-stmt>
                               | <external-stmt>
                               | <intent-stmt>
                               | <intrinsic-stmt>
                               | <namelist-stmt>
                               | <optional-stmt>
                               | <pointer-stmt>
                               | <protected-stmt>
                               | <save-stmt>
                               | <target-stmt>
                               | <volatile-stmt>
                               | <value-stmt>

    """

    subclass_names = [
        "Access_Stmt",
        "Allocatable_Stmt",
        "Asynchronous_Stmt",
        "Bind_Stmt",
        "Comment",
        "Common_Stmt",
        "Data_Stmt",
        "Dimension_Stmt",
        "Equivalence_Stmt",
        "External_Stmt",
        "Intent_Stmt",
        "Intrinsic_Stmt",
        "Namelist_Stmt",
        "Optional_Stmt",
        "Pointer_Stmt",
        "Cray_Pointer_Stmt",
        "Protected_Stmt",
        "Save_Stmt",
        "Target_Stmt",
        "Volatile_Stmt",
        "Value_Stmt",
    ]
