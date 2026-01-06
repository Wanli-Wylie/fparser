from fparser.two.utils import (
    Base,
)

class Do_Construct(Base):  # pylint: disable=invalid-name
    """
    R825::

        <do-construct> = <block-do-construct>
                         | <nonblock-do-construct>

    """

    subclass_names = ["Block_Do_Construct", "Nonblock_Do_Construct"]
