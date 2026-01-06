class Blank_Interp_Edit_Desc(STRINGBase):  # R1016
    """
    ::

        <blank-interp-edit-desc> = BN
                                 | BZ

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["BN", "BZ"], string)
