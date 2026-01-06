class Object_Name(Base):  # R505
    """
    ::

        <object-name> = <name>

    """

    subclass_names = ["Name"]


class Object_Name_List(SequenceBase):
    subclass_names = ["Object_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Object_Name, string)

    def __iter__(self):
        return iter(self.items)
