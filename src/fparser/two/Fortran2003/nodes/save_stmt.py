class Save_Stmt(StmtBase, WORDClsBase):  # R543
    """
    ::

        <save-stmt> = SAVE [ [ :: ] <saved-entity-list> ]

    """

    subclass_names = []
    use_names = ["Saved_Entity_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "SAVE", Saved_Entity_List, string, colons=True, require_cls=False
        )

    tostr = WORDClsBase.tostr_a
