from fparser.two.utils import (
    CALLBase,
)

from intent_spec import Intent_Spec

class Intent_Attr_Spec(CALLBase):  # R503.f
    """
    ::

        <intent-attr-spec> = INTENT ( <intent-spec> )

    """

    subclass_names = []
    use_names = ["Intent_Spec"]

    @staticmethod
    def match(string):
        return CALLBase.match("INTENT", Intent_Spec, string)
