from fparser.two.utils import (
    STRINGBase,
)

class Sign_Edit_Desc(STRINGBase):  # R1015
    """
    ::

        <sign-edit-desc> = SS
                           | SP
                           | S

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["SS", "SP", "S"], string)
