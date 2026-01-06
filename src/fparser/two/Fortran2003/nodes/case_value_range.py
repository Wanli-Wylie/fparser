from case_value import Case_Value

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


class Case_Value_Range_List(SequenceBase):
    subclass_names = ["Case_Value_Range"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Case_Value_Range, string)

    def __iter__(self):
        return iter(self.items)
