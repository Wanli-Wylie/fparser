from fparser.two.utils import (
    Base,
)

class Module_Subprogram(Base):  # R1108
    """
    ::

        <module-subprogram> = <function-subprogram>
                              | <subroutine-subprogram>

    """

    subclass_names = ["Function_Subprogram", "Subroutine_Subprogram"]
