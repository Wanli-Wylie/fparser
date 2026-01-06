from fparser.two.utils import (
    Base,
)

class Forall_Body_Construct(Base):  # R756
    """
    ::

        <forall-body-construct> = <forall-assignment-stmt>
                                  | <where-stmt>
                                  | <where-construct>
                                  | <forall-construct>
                                  | <forall-stmt>

    """

    subclass_names = [
        "Forall_Assignment_Stmt",
        "Where_Stmt",
        "Where_Construct",
        "Forall_Construct",
        "Forall_Stmt",
    ]
