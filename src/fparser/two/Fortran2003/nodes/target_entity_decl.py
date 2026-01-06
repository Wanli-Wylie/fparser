class Target_Entity_Decl(Entity_Decl):
    """
    ::

        <target-entity-decl> = <object-name> [ ( <array-spec> ) ]

    """

    subclass_names = []
    use_names = ["Object_Name", "Array_Spec"]

    @staticmethod
    def match(string):
        return Entity_Decl.match(string, target=True)


class Target_Entity_Decl_List(SequenceBase):
    subclass_names = ["Target_Entity_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Target_Entity_Decl, string)

    def __iter__(self):
        return iter(self.items)
