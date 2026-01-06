from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    BinaryOpBase,
)

from or_operand import Or_Operand

class Equiv_Operand(BinaryOpBase):  # R716
    """
    ::

        <equiv-operand> = [ <equiv-operand> <or-op> ] <or-operand>
        <or-op>  = .OR.

    """

    subclass_names = ["Or_Operand"]
    use_names = ["Equiv_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Equiv_Operand, pattern.or_op.named(), Or_Operand, string
        )
