from fparser.two.utils import (
    KeywordValueBase,
    SequenceBase,
)

from actual_arg import Actual_Arg
from keyword import Keyword

class Actual_Arg_Spec(KeywordValueBase):  # R1220
    """
    <actual-arg-spec> = [ <keyword> = ] <actual-arg>
    """

    subclass_names = ["Actual_Arg"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Actual_Arg, string)


class Actual_Arg_Spec_List(SequenceBase):
    subclass_names = ["Actual_Arg_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Actual_Arg_Spec, string)

    def __iter__(self):
        return iter(self.items)
