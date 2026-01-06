from fparser.two.utils import (
    Base,
)

class Executable_Construct(Base):  # R213
    # pylint: disable=invalid-name
    """
    Fortran 2003 rule R213::

        executable-construct is action-stmt
                             or associate-construct
                             or case-construct
                             or do-construct
                             or forall-construct
                             or if-construct
                             or select-type-construct
                             or where-construct

    """
    subclass_names = [
        "Action_Stmt",
        "Associate_Construct",
        "Case_Construct",
        "Do_Construct",
        "Forall_Construct",
        "If_Construct",
        "Select_Type_Construct",
        "Where_Construct",
    ]
