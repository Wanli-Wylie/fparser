class Case_Value_Range(SeparatorBase):  # R814
    """
    ::

        <case-value-range> = <case-value>
                             | <case-value> :
                             | : <case-value>
                             | <case-value> : <case-value>

    """

    subclass_names = ["Case_Value"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Case_Value, Case_Value, string)
