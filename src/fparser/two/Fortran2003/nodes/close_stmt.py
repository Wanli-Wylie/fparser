class Close_Stmt(StmtBase, CALLBase):  # R908
    """
    <close-stmt> = CLOSE ( <close-spec-list> )
    """

    subclass_names = []
    use_names = ["Close_Spec_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("CLOSE", Close_Spec_List, string, require_rhs=True)
