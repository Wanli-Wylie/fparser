from fparser.two.utils import (
    Base,
)

class Errmsg_Variable(Base):  # R626
    """
    ::

        <errmsg-variable> = <scalar-default-char-variable>

    """

    subclass_names = ["Scalar_Default_Char_Variable"]
