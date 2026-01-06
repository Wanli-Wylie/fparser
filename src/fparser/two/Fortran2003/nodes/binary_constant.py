from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    STRINGBase,
)

class Binary_Constant(STRINGBase):  # R412
    """
    ::

        <binary-constant> = B ' <digit> [ <digit> ]... '
                            | B \" <digit> [ <digit> ]... \"
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_binary_constant, string)
