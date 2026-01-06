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
