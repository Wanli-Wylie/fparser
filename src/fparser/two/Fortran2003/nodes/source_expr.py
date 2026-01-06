from fparser.two.utils import (
    Base,
)

class Source_Expr(Base):  # R627
    """
    ::

        <source-expr> = <expr>

    """

    subclass_names = ["Expr"]
