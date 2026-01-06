from fparser.two.utils import (
    Base,
)

class N(Base):  # R1014
    """
    ::

        <n> = <int-literal-constant> == <digit-string>

    Subject to::

        C1010, C1011: <n> is positive and without kind parameter.

    """

    subclass_names = ["Digit_String"]
