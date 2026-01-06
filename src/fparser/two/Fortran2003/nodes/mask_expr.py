from fparser.two.utils import (
    Base,
)

class Mask_Expr(Base):  # R748
    """
    <mask-expr> = <logical-expr>
    """

    subclass_names = ["Logical_Expr"]


class Scalar_Mask_Expr(Base):
    subclass_names = ["Mask_Expr"]
