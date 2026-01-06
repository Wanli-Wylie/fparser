class Data_Stmt_Value(Base):  # R530
    """
    ::

        <data-stmt-value> = [ <data-stmt-repeat> * ] <data-stmt-constant>

    """

    subclass_names = ["Data_Stmt_Constant"]
    use_names = ["Data_Stmt_Repeat"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        s = line.split("*", 1)
        if len(s) != 2:
            return
        lhs = repmap(s[0].rstrip())
        rhs = repmap(s[1].lstrip())
        if not lhs or not rhs:
            return
        return Data_Stmt_Repeat(lhs), Data_Stmt_Constant(rhs)

    def tostr(self):
        return "%s * %s" % self.items
