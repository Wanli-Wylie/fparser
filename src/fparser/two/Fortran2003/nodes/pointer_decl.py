class Pointer_Decl(CallBase):  # R541
    """
    ::

        <pointer-decl> = <object-name> [ ( <deferred-shape-spec-list> ) ]
                         | <proc-entity-name>

    """

    subclass_names = ["Proc_Entity_Name", "Object_Name"]
    use_names = ["Deferred_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Object_Name, Deferred_Shape_Spec_List, string, require_rhs=True
        )
