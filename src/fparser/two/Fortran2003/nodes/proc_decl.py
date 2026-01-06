class Proc_Decl(BinaryOpBase):  # R1214
    """
    ::

        <proc-decl> = <procedure-entity-name> [ => <null-init> ]

    Attributes::

        items : (Procedure_Entity_Name, Null_Init)

    """

    subclass_names = ["Procedure_Entity_Name"]
    use_names = ["Null_Init"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Procedure_Entity_Name, "=>", Null_Init, string)
