class Ac_Value(Base):  # R469
    """
    ::

        <ac-value> = <expr>
                     | <ac-implied-do>

    """

    subclass_names = ["Ac_Implied_Do", "Expr"]
