class External_Stmt(StmtBase, WORDClsBase):  # R1210
    """
    ::

        <external-stmt> = EXTERNAL [ :: ] <external-name-list>

    """

    subclass_names = []
    use_names = ["External_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "EXTERNAL", External_Name_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
