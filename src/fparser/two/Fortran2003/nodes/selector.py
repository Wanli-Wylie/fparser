from fparser.two.utils import (
    Base,
)

class Selector(Base):  # R819
    """
    ::

        <selector> = <expr>
                     | <variable>
    """

    subclass_names = ["Expr", "Variable"]
