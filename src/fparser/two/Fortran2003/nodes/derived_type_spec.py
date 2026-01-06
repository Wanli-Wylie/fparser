class Derived_Type_Spec(CallBase):  # R455
    """
    ::

        <derived-type-spec> = <type-name> [ ( <type-param-spec-list> ) ]

    """

    subclass_names = ["Type_Name"]
    use_names = ["Type_Param_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(Type_Name, Type_Param_Spec_List, string)
