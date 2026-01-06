from fparser.two.utils import (
    Base,
)

class Boz_Literal_Constant(Base):  # R411
    """
    ::

        <boz-literal-constant> = <binary-constant>
                                 | <octal-constant>
                                 | <hex-constant>
    """

    subclass_names = ["Binary_Constant", "Octal_Constant", "Hex_Constant"]
