from fparser.two.utils import (
    Base,
)

class Variable_Name(Base):  # R602
    """
    ::

        <variable-name> = <name>

    """

    subclass_names = ["Name"]
