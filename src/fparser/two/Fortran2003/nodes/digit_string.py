from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    NumberBase,
)

class Digit_String(NumberBase):
    """
    ::

        <digit-string> = <digit> [ <digit> ]...

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_digit_string_named, string)
