from fparser.two.utils import (
    Base,
)

class External_Subprogram(Base):  # R203
    """
    Fortran2003 Rule R203::

        <external-subprogram> = <function-subprogram>
                                | <subroutine-subprogram>
    """

    subclass_names = ["Comment", "Function_Subprogram", "Subroutine_Subprogram"]
