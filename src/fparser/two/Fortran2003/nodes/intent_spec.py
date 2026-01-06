from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    STRINGBase,
)

class Intent_Spec(STRINGBase):  # R517
    """
    ::

        <intent-spec> = IN
                        | OUT
                        | INOUT

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_intent_spec, string)
