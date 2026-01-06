from fparser.two.utils import (
    STRINGBase,
)

class Access_Spec(STRINGBase):  # R508
    """
    Fortran2003 Rule R508::

        <access-spec> = PUBLIC
                        | PRIVATE

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["PUBLIC", "PRIVATE"], string)
