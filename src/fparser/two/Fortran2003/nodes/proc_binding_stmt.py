from fparser.two.utils import (
    Base,
)

class Proc_Binding_Stmt(Base):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R450::

        <proc-binding-stmt> = <specific-binding>
                              | <generic-binding>
                              | <final-binding>

    Specifies the procedure binding for the type-bound procedures
    within a derived type.

    """

    subclass_names = ["Specific_Binding", "Generic_Binding", "Final_Binding"]
