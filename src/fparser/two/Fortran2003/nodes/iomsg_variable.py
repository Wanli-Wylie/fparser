from fparser.two.utils import (
    Base,
)

class Iomsg_Variable(Base):  # R907
    """
    <iomsg-variable> = <scalar-default-char-variable>
    """

    subclass_names = ["Scalar_Default_Char_Variable"]
