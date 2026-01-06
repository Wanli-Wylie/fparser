from fparser.two.utils import (
    KeywordValueBase,
    SequenceBase,
)

from keyword import Keyword
from type_param_value import Type_Param_Value

class Type_Param_Spec(KeywordValueBase):  # R456
    """
    ::

        <type-param-spec> = [ <keyword> = ] <type-param-value>

    """

    subclass_names = ["Type_Param_Value"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Type_Param_Value, string)


class Type_Param_Spec_List(SequenceBase):
    subclass_names = ["Type_Param_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Param_Spec, string)

    def __iter__(self):
        return iter(self.items)
