class Case_Selector(Base):  # R813
    """
    ::

        <case-selector> = ( <case-value-range-list> )
                          | DEFAULT

    """

    subclass_names = []
    use_names = ["Case_Value_Range_List"]

    @staticmethod
    def match(string):
        if len(string) == 7 and string.upper() == "DEFAULT":
            return (None,)
        if not (string.startswith("(") and string.endswith(")")):
            return
        return (Case_Value_Range_List(string[1:-1].strip()),)

    def tostr(self):
        if self.items[0] is None:
            return "DEFAULT"
        return "(%s)" % (self.items[0])
