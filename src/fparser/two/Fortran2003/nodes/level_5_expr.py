from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    BinaryOpBase,
)

from equiv_operand import Equiv_Operand

class Level_5_Expr(BinaryOpBase):  # R717
    """
    ::

        <level-5-expr> = [ <level-5-expr> <equiv-op> ] <equiv-operand>
        <equiv-op> = .EQV.
                   | .NEQV.

    """

    subclass_names = ["Equiv_Operand"]
    use_names = ["Level_5_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_5_Expr, pattern.equiv_op.named(), Equiv_Operand, string
        )
