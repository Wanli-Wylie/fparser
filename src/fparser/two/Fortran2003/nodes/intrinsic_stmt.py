class Intrinsic_Stmt(StmtBase, WORDClsBase):  # R1216
    """
    ::

        <intrinsic-stmt> = INTRINSIC [ :: ] <intrinsic-procedure-name-list>

    """

    subclass_names = []
    use_names = ["Intrinsic_Procedure_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "INTRINSIC",
            Intrinsic_Procedure_Name_List,
            string,
            colons=True,
            require_cls=True,
        )

    tostr = WORDClsBase.tostr_a
