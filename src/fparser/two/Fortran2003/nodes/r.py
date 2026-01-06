from fparser.two.utils import (
    Base,
)

class R(Base):  # R1004
    """
    ::

        <r> = <int-literal-constant>

    Notes::

        C1003, C1004: <r> shall be positive and without kind parameter specified.
    """

    subclass_names = ["Digit_String"]
