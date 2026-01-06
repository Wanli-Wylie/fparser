class Pointer_Object(Base):  # R634
    """
    ::

        <pointer-object> = <variable-name>
                           | <structure-component>
                           | <proc-pointer-name>

    """

    subclass_names = ["Variable_Name", "Structure_Component", "Proc_Pointer_Name"]


class Pointer_Object_List(SequenceBase):
    subclass_names = ["Pointer_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Pointer_Object, string)

    def __iter__(self):
        return iter(self.items)
