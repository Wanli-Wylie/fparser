class Logical_Initialization_Expr(Base):  # R733
    """
    ::

        <logical-initialization-expr> = <logical-expr>

    """

    subclass_names = ["Logical_Expr"]


class Scalar_Logical_Initialization_Expr(Base):
    subclass_names = ["Logical_Initialization_Expr"]
