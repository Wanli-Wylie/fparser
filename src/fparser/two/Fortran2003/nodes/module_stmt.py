class Module_Stmt(StmtBase, WORDClsBase, ScopingRegionMixin):  # R1105
    """
    <module-stmt> = MODULE <module-name>
    """

    subclass_names = []
    use_names = ["Module_Name"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("MODULE", Module_Name, string, require_cls=True)

    def get_name(self):
        return self.items[1]
