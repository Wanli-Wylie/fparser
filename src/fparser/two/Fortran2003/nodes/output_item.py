from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Output_Item(Base):  # R916
    """
    ::

        <output-item> = <expr>
                        | <io-implied-do>
    """

    subclass_names = ["Expr", "Io_Implied_Do"]


class Output_Item_List(SequenceBase):
    subclass_names = ["Output_Item"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Output_Item, string)

    def __iter__(self):
        return iter(self.items)
