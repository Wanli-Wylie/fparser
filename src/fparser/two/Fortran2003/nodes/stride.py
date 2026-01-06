from fparser.two.utils import (
    Base,
)

class Stride(Base):  # R621
    """
    ::

        <stride> = <scalar-int-expr>

    """

    subclass_names = ["Scalar_Int_Expr"]
