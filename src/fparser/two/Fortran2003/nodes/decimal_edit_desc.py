class Decimal_Edit_Desc(STRINGBase):  # R1018
    """
    <decimal-edit-desc> = DC
                          | DP
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["DC", "DP"], string)
