class Data_I_Do_Object(Base):  # R528
    """
    ::

        <data-i-do-object> = <array-element>
                             | <scalar-structure-component>
                             | <data-implied-do>

    """

    subclass_names = ["Array_Element", "Scalar_Structure_Component", "Data_Implied_Do"]


class Data_I_Do_Object_List(SequenceBase):
    subclass_names = ["Data_I_Do_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Data_I_Do_Object, string)

    def __iter__(self):
        return iter(self.items)
