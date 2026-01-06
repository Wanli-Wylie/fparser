from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    Base,
)

from imag_part import Imag_Part
from real_part import Real_Part

class Complex_Literal_Constant(Base):  # R421
    """
    ::

        <complex-literal-constant> = ( <real-part>, <imag-part> )
    """

    subclass_names = []
    use_names = ["Real_Part", "Imag_Part"]

    @staticmethod
    def match(string):
        if not string or string[0] + string[-1] != "()":
            return
        if not pattern.abs_complex_literal_constant.match(string):
            return
        r, i = string[1:-1].split(",")
        return Real_Part(r.strip()), Imag_Part(i.strip())

    def tostr(self):
        return "(%s, %s)" % tuple(self.items)
