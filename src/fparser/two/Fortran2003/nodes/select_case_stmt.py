from case_expr import Case_Expr

class Select_Case_Stmt(StmtBase, CALLBase):  # R809
    """
    ::

        <select-case-stmt> = [ <case-construct-name> : ]
            SELECT CASE ( <case-expr> )

    """

    subclass_names = []
    use_names = ["Case_Construct_Name", "Case_Expr"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "SELECT":
            return
        line = string[6:].lstrip()
        if line[:4].upper() != "CASE":
            return
        line = line[4:].lstrip()
        if not line or line[0] + line[-1] != "()":
            return
        line = line[1:-1].strip()
        return (Case_Expr(line),)

    def tostr(self):
        return "SELECT CASE (%s)" % (self.items[0])

    def get_start_name(self):
        return self.item.name
