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
