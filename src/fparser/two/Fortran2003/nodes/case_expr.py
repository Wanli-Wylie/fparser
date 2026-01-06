from fparser.two.utils import (
    Base,
)

class Case_Expr(Base):  # R812
    """
    ::

        <case-expr> = <scalar-int-expr>
                      | <scalar-char-expr>
                      | <scalar-logical-expr>

    """

    subclass_names = []
    subclass_names = ["Scalar_Int_Expr", "Scalar_Char_Expr", "Scalar_Logical_Expr"]
