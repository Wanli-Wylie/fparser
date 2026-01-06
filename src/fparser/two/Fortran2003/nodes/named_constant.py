from fparser.two.utils import (
    Base,
)

class Named_Constant(Base):  # R307
    """
    ::
        <named-constant> = <name>

    """

    subclass_names = ["Name"]
