class Case_Value(Base):  # R815
    """
    ::

        <case-value> = <scalar-int-initialization-expr>
                       | <scalar-char-initialization-expr>
                       | <scalar-logical-initialization-expr>

    """

    subclass_names = [
        "Scalar_Int_Initialization_Expr",
        "Scalar_Char_Initialization_Expr",
        "Scalar_Logical_Initialization_Expr",
    ]
