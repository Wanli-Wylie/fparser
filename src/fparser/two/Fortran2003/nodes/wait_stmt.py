class Wait_Stmt(StmtBase, CALLBase):  # R921
    """
    <wait-stmt> = WAIT ( <wait-spec-list> )
    """

    subclass_names = []
    use_names = ["Wait_Spec_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("WAIT", Wait_Spec_List, string, require_rhs=True)
