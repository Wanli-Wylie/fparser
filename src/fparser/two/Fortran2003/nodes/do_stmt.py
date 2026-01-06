from fparser.two.utils import (
    Base,
)

class Do_Stmt(Base):  # pylint: disable=invalid-name
    """
    R827::

        <do-stmt> = <label-do-stmt>
                    | <nonlabel-do-stmt>

    """

    subclass_names = ["Label_Do_Stmt", "Nonlabel_Do_Stmt"]
