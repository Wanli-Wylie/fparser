class Sequence_Stmt(STRINGBase):  # R434
    """
    ::

        <sequence-stmt> = SEQUENCE

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match("SEQUENCE", string)
