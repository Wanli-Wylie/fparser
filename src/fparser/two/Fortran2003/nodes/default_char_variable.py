class Default_Char_Variable(Base):  # R607
    """
    ::

        <default-char-variable> = <variable>

    """

    subclass_names = ["Variable"]


class Scalar_Default_Char_Variable(Base):
    subclass_names = ["Default_Char_Variable"]
