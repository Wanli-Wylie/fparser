from forall_header import Forall_Header

class Forall_Construct_Stmt(StmtBase, WORDClsBase):  # R753
    """
    ::

        <forall-construct-stmt> = [ <forall-construct-name> : ]
            FORALL <forall-header>

    """

    subclass_names = []
    use_names = ["Forall_Construct_Name", "Forall_Header"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("FORALL", Forall_Header, string, require_cls=True)

    def get_start_name(self):
        return self.item.name
