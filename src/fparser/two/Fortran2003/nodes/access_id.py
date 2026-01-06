class Access_Id(Base):  # R519
    """
    Fortran2003 Rule R519::

        <access-id> = <use-name>
                      | <generic-spec>

    """

    subclass_names = ["Use_Name", "Generic_Spec"]


class Access_Id_List(SequenceBase):
    subclass_names = ["Access_Id"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Access_Id, string)

    def __iter__(self):
        return iter(self.items)
