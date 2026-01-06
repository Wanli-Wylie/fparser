from fparser.two.utils import (
    STRINGBase,
)

class Round_Edit_Desc(STRINGBase):  # R1017
    """
    ::

        <round-edit-desc> = RU
                            | RD
                            | RZ
                            | RN
                            | RC
                            | RP

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["RU", "RD", "RZ", "RN", "RC", "RP"], string)
