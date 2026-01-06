from fparser.two.utils import (
    Base,
)

class Proc_Pointer_Name(Base):  # R545
    """
    ::

        <proc-pointer-name> = <name>

    """

    subclass_names = ["Name"]
