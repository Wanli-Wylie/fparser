class Continue_Stmt(StmtBase, STRINGBase):  # R848
    """
    <continue-stmt> = CONTINUE
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match("CONTINUE", string)

    def get_end_label(self):
        return self.item.label
