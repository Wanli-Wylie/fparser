class End_Forall_Stmt(EndStmtBase):  # R758
    """
    <end-forall-stmt> = END FORALL [ <forall-construct-name> ]
    """

    subclass_names = []
    use_names = ["Forall_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "FORALL", Forall_Construct_Name, string, require_stmt_type=True
        )
