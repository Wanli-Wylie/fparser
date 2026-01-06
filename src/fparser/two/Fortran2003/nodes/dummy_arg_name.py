class Dummy_Arg_Name(Base):  # R1226
    """
    <dummy-arg-name> = <name>
    """

    subclass_names = ["Name"]


class Dummy_Arg_Name_List(SequenceBase):
    subclass_names = ["Dummy_Arg_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Dummy_Arg_Name, string)

    def __iter__(self):
        return iter(self.items)
