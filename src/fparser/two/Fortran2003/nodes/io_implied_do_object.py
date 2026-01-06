class Io_Implied_Do_Object(Base):  # R918
    """
    ::

        <io-implied-do-object> = <input-item>
                                 | <output-item>

    """

    subclass_names = ["Input_Item", "Output_Item"]


class Io_Implied_Do_Object_List(SequenceBase):
    subclass_names = ["Io_Implied_Do_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Io_Implied_Do_Object, string)

    def __iter__(self):
        return iter(self.items)
