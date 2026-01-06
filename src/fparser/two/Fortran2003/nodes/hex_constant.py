from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    STRINGBase,
)

class Hex_Constant(STRINGBase):  # R414
    """
    ::

        <hex-constant> = Z ' <digit> [ <digit> ]... '
                         | Z \" <digit> [ <digit> ]... \"
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_hex_constant, string)
