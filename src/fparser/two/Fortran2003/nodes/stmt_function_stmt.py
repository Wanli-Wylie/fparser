class Stmt_Function_Stmt(StmtBase):  # R1238
    """
    ::

        <stmt-function-stmt>
        = <function-name> ( [ <dummy-arg-name-list> ] ) = Scalar_Expr

    """

    subclass_names = []
    use_names = ["Function_Name", "Dummy_Arg_Name_List", "Scalar_Expr"]

    @staticmethod
    def match(string):
        i = string.find("=")
        if i == -1:
            return
        expr = string[i + 1 :].lstrip()
        if not expr:
            return
        line = string[:i].rstrip()
        if not line or not line.endswith(")"):
            return
        i = line.find("(")
        if i == -1:
            return
        name = line[:i].rstrip()
        if not name:
            return
        args = line[i + 1 : -1].strip()
        if args:
            return Function_Name(name), Dummy_Arg_Name_List(args), Scalar_Expr(expr)
        return Function_Name(name), None, Scalar_Expr(expr)

    def tostr(self):
        if self.items[1] is None:
            return "%s () = %s" % (self.items[0], self.items[2])
        return "%s (%s) = %s" % self.items
