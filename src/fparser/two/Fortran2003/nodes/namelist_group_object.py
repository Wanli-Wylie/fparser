class Namelist_Group_Object(Base):  # R553
    """
    ::

        <namelist-group-object> = <variable-name>

    """

    subclass_names = ["Variable_Name"]


class Namelist_Group_Object_List(SequenceBase):
    subclass_names = ["Namelist_Group_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Namelist_Group_Object, string)

    def __iter__(self):
        return iter(self.items)
