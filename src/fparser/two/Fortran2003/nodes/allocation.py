class Allocation(CallBase):  # R628
    """
    ::

        <allocation> = <allocate-object> [ ( <allocate-shape-spec-list> ) ]
                     | <variable-name>

    """

    subclass_names = ["Variable_Name", "Allocate_Object"]
    use_names = ["Allocate_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Allocate_Object, Allocate_Shape_Spec_List, string, require_rhs=True
        )
