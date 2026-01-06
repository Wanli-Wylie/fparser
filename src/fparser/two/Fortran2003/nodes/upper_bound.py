from fparser.two.utils import (
    Base,
)

class Upper_Bound(Base):  # R513
    """
    ::

        <upper-bound> = <specification-expr>

    """

    subclass_names = ["Specification_Expr"]
