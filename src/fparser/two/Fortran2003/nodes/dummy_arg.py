class Dummy_Arg(StringBase):  # R1233
    """
    ::

        <dummy-arg> = <dummy-arg-name>
                      | *

    """

    subclass_names = ["Dummy_Arg_Name"]

    @staticmethod
    def match(string):
        return StringBase.match("*", string)


class Dummy_Arg_List(SequenceBase):
    subclass_names = ["Dummy_Arg"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Dummy_Arg, string)

    def __iter__(self):
        return iter(self.items)
