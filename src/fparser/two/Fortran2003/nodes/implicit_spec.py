class Implicit_Spec(CallBase):  # R550
    """
    ::

        <implicit-spec> = <declaration-type-spec> ( <letter-spec-list> )

    """

    subclass_names = []
    use_names = ["Declaration_Type_Spec", "Letter_Spec_List"]

    @staticmethod
    def match(string):
        if not string.endswith(")"):
            return
        i = string.rfind("(")
        if i == -1:
            return
        s1 = string[:i].rstrip()
        s2 = string[i + 1 : -1].strip()
        if not s1 or not s2:
            return
        return Declaration_Type_Spec(s1), Letter_Spec_List(s2)


class Implicit_Spec_List(SequenceBase):
    subclass_names = ["Implicit_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Implicit_Spec, string)

    def __iter__(self):
        return iter(self.items)
