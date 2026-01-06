from fparser.two.utils import (
    Base,
)

class Vector_Subscript(Base):  # R622
    """
    ::

        <vector-subscript> = <int-expr>

    """

    subclass_names = ["Int_Expr"]
