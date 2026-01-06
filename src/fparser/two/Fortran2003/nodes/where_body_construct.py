from fparser.two.utils import (
    Base,
)

class Where_Body_Construct(Base):  # R746
    """
    ::

        <where-body-construct> = <where-assignment-stmt>
                                 | <where-stmt>
                                 | <where-construct>

    """

    subclass_names = ["Where_Assignment_Stmt", "Where_Stmt", "Where_Construct"]
