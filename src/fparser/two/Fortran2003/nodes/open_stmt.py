class Open_Stmt(StmtBase, CALLBase):  # R904
    """
    R904 is:

    open-stmt is OPEN ( connect-spec-list )
    """

    subclass_names = []
    use_names = ["Connect_Spec_List"]

    @staticmethod
    def match(string):
        # The Connect_Spec_List class is generated automatically
        # by code at the end of this module
        return CALLBase.match("OPEN", Connect_Spec_List, string, require_rhs=True)
