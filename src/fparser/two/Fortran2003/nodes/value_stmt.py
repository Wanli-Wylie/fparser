from dummy_arg_name import Dummy_Arg_Name_List

class Value_Stmt(StmtBase, WORDClsBase):  # R547
    """
    ::

        <value-stmt> = VALUE [ :: ] <dummy-arg-name-list>

    """

    subclass_names = []
    use_names = ["Dummy_Arg_Name_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "VALUE", Dummy_Arg_Name_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
