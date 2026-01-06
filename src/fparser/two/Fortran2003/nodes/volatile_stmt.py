from object_name import Object_Name_List

class Volatile_Stmt(StmtBase, WORDClsBase):  # R548
    """
    ::

        <volatile-stmt> = VOLATILE [ :: ] <object-name-list>

    """

    subclass_names = []
    use_names = ["Object_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "VOLATILE", Object_Name_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
