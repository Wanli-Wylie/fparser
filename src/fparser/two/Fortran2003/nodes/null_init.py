class Null_Init(STRINGBase):  # R507
    """
    ::

        null-init is function-reference

    where::

        function-reference shall be a reference to the NULL
                           intrinsic function with no arguments.

    """

    subclass_names = ["Function_Reference"]

    @staticmethod
    def match(string):
        return STRINGBase.match("NULL", string)
