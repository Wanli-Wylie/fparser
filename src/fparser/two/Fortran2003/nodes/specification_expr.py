from fparser.two.utils import (
    Base,
)

class Specification_Expr(Base):  # R729
    """
    ::

        <specification-expr> = <scalar-int-expr>

    """

    subclass_names = ["Scalar_Int_Expr"]
