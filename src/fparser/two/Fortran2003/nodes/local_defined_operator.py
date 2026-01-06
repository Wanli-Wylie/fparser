class Local_Defined_Operator(Base):  # R1114
    """
    ::

        <local-defined-operator> = <defined-unary-op>
                                   | <defined-binary-op>

    """

    subclass_names = ["Defined_Unary_Op", "Defined_Binary_Op"]
