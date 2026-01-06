from fparser.two.utils import (
    Base,
)

class Nonblock_Do_Construct(Base):  # pylint: disable=invalid-name
    """
    R835::

        <nonblock-do-stmt> = <action-term-do-construct>
                             | <outer-shared-do-construct>

    """

    subclass_names = ["Action_Term_Do_Construct", "Outer_Shared_Do_Construct"]
