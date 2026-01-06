class W(Base):  # R1006
    """
    ::

        w is int-literal-constant == digit-string

    Subject to constraints::

        C1006, C1007: w is zero or postive and without kind parameters.

    """

    subclass_names = ["Digit_String"]
