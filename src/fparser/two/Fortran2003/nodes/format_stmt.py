class Format_Stmt(StmtBase, WORDClsBase):  # R1001
    """
    <format-stmt> = FORMAT <format-specification>
    """

    subclass_names = []
    use_names = ["Format_Specification"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "FORMAT", Format_Specification, string, require_cls=True
        )
