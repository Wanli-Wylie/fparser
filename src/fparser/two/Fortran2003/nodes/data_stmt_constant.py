class Data_Stmt_Constant(Base):  # R532
    """
    Fortran 2003 Rule R532::

        <data-stmt-constant> = <scalar-constant>
                               | <scalar-constant-subobject>
                               | <signed-int-literal-constant>
                               | <signed-real-literal-constant>
                               | <null-init>
                               | <structure-constructor>

    """

    subclass_names = [
        "Scalar_Constant",
        "Scalar_Constant_Subobject",
        "Signed_Int_Literal_Constant",
        "Signed_Real_Literal_Constant",
        "Null_Init",
        "Structure_Constructor",
    ]
