from fparser.two.utils import (
    Base,
)

class Upper_Bound_Expr(Base):  # R632
    """
    ::

        <upper-bound-expr> = <scalar-int-expr>

    """

    subclass_names = ["Scalar_Int_Expr"]
