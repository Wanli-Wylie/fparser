from fparser.two.utils import (
    Base,
)

class Variable(Base):  # R601
    """
    ::

        <variable> = <designator>

    """

    subclass_names = ["Designator"]
