class Object_Name_Deferred_Shape_Spec_List_Item(CallBase):
    """
    ::

        <..> =  <object-name> [ ( <deferred-shape-spec-list> ) ]

    """

    subclass_names = ["Object_Name"]
    use_names = ["Deferred_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Object_Name, Deferred_Shape_Spec_List, string, require_rhs=True
        )
