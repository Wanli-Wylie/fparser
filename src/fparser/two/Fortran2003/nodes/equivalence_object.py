class Equivalence_Object(Base):  # R556
    """
    ::

        <equivalence-object> = <variable-name>
                               | <array-element>
                               | <substring>

    """

    subclass_names = ["Variable_Name", "Array_Element", "Substring"]


class Equivalence_Object_List(SequenceBase):
    subclass_names = ["Equivalence_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Equivalence_Object, string)

    def __iter__(self):
        return iter(self.items)
