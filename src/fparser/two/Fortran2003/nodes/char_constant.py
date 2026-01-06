class Char_Constant(Base):  # R309
    """
    ::

        <char-constant> = <constant>
    """

    subclass_names = ["Constant"]


class Scalar_Char_Constant(Base):
    subclass_names = ["Char_Constant"]
