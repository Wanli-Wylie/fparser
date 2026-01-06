from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    NumberBase,
)

class Signed_Real_Literal_Constant(NumberBase):  # R416
    """
    ::

        <signed-real-literal-constant> = [ <sign> ] <real-literal-constant>
    """

    subclass_names = ["Real_Literal_Constant"]  # never used

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_signed_real_literal_constant_named, string)
