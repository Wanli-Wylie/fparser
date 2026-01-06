from fparser.two.utils import (
    Base,
)

class End_Do(Base):  # pylint: disable=invalid-name
    """
    R833::

        <end-do> = <end-do-stmt>
                   | <continue-stmt>

    """

    subclass_names = ["End_Do_Stmt", "Continue_Stmt"]
