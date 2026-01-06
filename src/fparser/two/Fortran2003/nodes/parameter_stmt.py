from named_constant_def import Named_Constant_Def_List

class Parameter_Stmt(StmtBase, CALLBase):  # R538
    """
    ::

        <parameter-stmt> = PARAMETER ( <named-constant-def-list> )

    """

    subclass_names = []
    use_names = ["Named_Constant_Def_List"]

    @staticmethod
    def match(string):
        return CALLBase.match(
            "PARAMETER", Named_Constant_Def_List, string, require_rhs=True
        )
