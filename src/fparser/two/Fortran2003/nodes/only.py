class Only(Base):  # R1112
    """
    ::

        <only> = <generic-spec>
                 | <only-use-name>
                 | <rename>

    """

    subclass_names = ["Generic_Spec", "Only_Use_Name", "Rename"]


class Only_List(SequenceBase):
    subclass_names = ["Only"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Only, string)

    def __iter__(self):
        return iter(self.items)
