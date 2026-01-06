class Parent_String(Base):  # R610
    """
    ::

        <parent-string> = <scalar-variable-name>
                          | <array-element>
                          | <scalar-structure-component>
                          | <scalar-constant>

    """

    subclass_names = [
        "Scalar_Variable_Name",
        "Array_Element",
        "Scalar_Structure_Component",
        "Scalar_Constant",
    ]
