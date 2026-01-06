from fparser.two.utils import (
    Base,
)

class Literal_Constant(Base):  # R306
    """
    ::

        <literal-constant> = <int-literal-constant>
                             | <real-literal-constant>
                             | <complex-literal-constant>
                             | <logical-literal-constant>
                             | <char-literal-constant>
                             | <boz-literal-constant>
    """

    subclass_names = [
        "Int_Literal_Constant",
        "Real_Literal_Constant",
        "Complex_Literal_Constant",
        "Logical_Literal_Constant",
        "Char_Literal_Constant",
        "Boz_Literal_Constant",
    ]
