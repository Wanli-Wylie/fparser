from fparser.two.utils import (
    Base,
)

class Logical_Variable(Base):  # R604
    """
    ::

        <logical-variable> = <variable>

    """

    subclass_names = ["Variable"]
