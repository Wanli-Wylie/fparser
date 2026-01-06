from fparser.two.utils import (
    Base,
)

class Char_Variable(Base):  # R606
    """
    ::

        <char-variable> = <variable>

    """

    subclass_names = ["Variable"]
