class Input_Item(Base):  # R915
    """
    ::

        <input-item> = <variable>
                       | <io-implied-do>

    """

    subclass_names = ["Variable", "Io_Implied_Do"]


class Input_Item_List(SequenceBase):
    subclass_names = ["Input_Item"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Input_Item, string)

    def __iter__(self):
        return iter(self.items)
