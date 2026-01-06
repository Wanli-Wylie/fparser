class Proc_Component_Attr_Spec(STRINGBase):  # R446
    """
    ::

        <proc-component-attr-spec> = POINTER
                                     | PASS [ ( <arg-name> ) ]
                                     | NOPASS
                                     | <access-spec>

    """

    subclass_names = ["Access_Spec", "Proc_Component_PASS_Arg_Name"]

    @staticmethod
    def match(string):
        return STRINGBase.match(["POINTER", "PASS", "NOPASS"], string.upper())


class Proc_Component_Attr_Spec_List(SequenceBase):
    subclass_names = ["Proc_Component_Attr_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Proc_Component_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)
