class Forall_Assignment_Stmt(Base):  # R757
    """
    ::

        <forall-assignment-stmt> = <assignment-stmt>
                                   | <pointer-assignment-stmt>

    """

    subclass_names = ["Assignment_Stmt", "Pointer_Assignment_Stmt"]
