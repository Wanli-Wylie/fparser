from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    NumberBase,
)

class Logical_Literal_Constant(NumberBase):  # R428
    """
    ::

        <logical-literal-constant> = .TRUE. [ _ <kind-param> ]
                                     | .FALSE. [ _ <kind-param> ]
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_logical_literal_constant_named, string)
