from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    STRINGBase,
)

class Octal_Constant(STRINGBase):  # R413
    """
    ::

        <octal-constant> = O ' <digit> [ <digit> ]... '
                           | O \" <digit> [ <digit> ]... \"
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_octal_constant, string)
