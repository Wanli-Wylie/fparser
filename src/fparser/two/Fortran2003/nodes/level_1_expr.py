from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    UnaryOpBase,
)

from primary import Primary

class Level_1_Expr(UnaryOpBase):  # R702
    """
    ::

        <level-1-expr> = [ <defined-unary-op> ] <primary>
        <defined-unary-op> = . <letter> [ <letter> ]... .

    """

    subclass_names = ["Primary"]
    use_names = []

    @staticmethod
    def match(string):
        return UnaryOpBase.match(pattern.defined_unary_op.named(), Primary, string)
