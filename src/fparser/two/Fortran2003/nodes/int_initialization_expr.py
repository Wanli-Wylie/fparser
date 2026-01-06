from fparser.two.utils import (
    Base,
)

class Int_Initialization_Expr(Base):  # R732
    """
    ::

        <int-initialization-expr> = <int-expr>

    """

    subclass_names = ["Int_Expr"]


class Scalar_Int_Initialization_Expr(Base):
    subclass_names = ["Int_Initialization_Expr"]
