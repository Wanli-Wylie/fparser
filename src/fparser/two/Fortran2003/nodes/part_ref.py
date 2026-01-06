class Part_Ref(CallBase):  # R613
    """
    ::

        <part-ref> = <part-name> [ ( <section-subscript-list> ) ]

    """

    subclass_names = ["Part_Name"]
    use_names = ["Section_Subscript_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Part_Name, Section_Subscript_List, string, require_rhs=True
        )
