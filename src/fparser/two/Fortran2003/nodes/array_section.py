class Array_Section(CallBase):  # R617
    """
    ::

        <array-section> = <data-ref> [ ( <substring-range> ) ]

    """

    subclass_names = ["Data_Ref"]
    use_names = ["Substring_Range"]

    @staticmethod
    def match(string):
        return CallBase.match(Data_Ref, Substring_Range, string, require_rhs=True)
