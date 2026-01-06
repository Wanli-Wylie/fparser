from name import Entity_Name_List

class Protected_Stmt(StmtBase, WORDClsBase):  # R542
    """
    ::

        <protected-stmt> = PROTECTED [ :: ] <entity-name-list>

    """

    subclass_names = []
    use_names = ["Entity_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "PROTECTED", Entity_Name_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
