from fparser.two.utils import (
    Base,
)

class Keyword(Base):  # R215
    """
    ::

        <keyword> = <name>

    """

    subclass_names = ["Name"]
