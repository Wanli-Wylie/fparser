from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Ac_Value(Base):  # R469
    """
    ::

        <ac-value> = <expr>
                     | <ac-implied-do>

    """

    subclass_names = ["Ac_Implied_Do", "Expr"]


class Ac_Value_List(SequenceBase):
    subclass_names = ["Ac_Value"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Ac_Value, string)

    def __iter__(self):
        return iter(self.items)
