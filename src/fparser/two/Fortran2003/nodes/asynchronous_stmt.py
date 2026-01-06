class Asynchronous_Stmt(StmtBase, WORDClsBase):  # R521
    """
    Fortran2003 Rule R521::

        <asynchronous-stmt> = ASYNCHRONOUS [ :: ] <object-name-list>

    """

    subclass_names = []
    use_names = ["Object_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "ASYNCHRONOUS", Object_Name_List, string, colons=True, require_cls=True
        )
