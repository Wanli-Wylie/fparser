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
