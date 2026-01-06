class Type_Param_Def_Stmt(StmtBase):  # R435
    """
    ::

        <type-param-def-stmt> = INTEGER [ <kind-selector> ] ,
            <type-param-attr-spec> :: <type-param-decl-list>

    """

    subclass_names = []
    use_names = ["Kind_Selector", "Type_Param_Attr_Spec", "Type_Param_Decl_List"]

    @staticmethod
    def match(string):
        if string[:7].upper() != "INTEGER":
            return
        line, repmap = string_replace_map(string[7:].lstrip())
        if not line:
            return
        i = line.find(",")
        if i == -1:
            return
        kind_selector = repmap(line[:i].rstrip()) or None
        line = repmap(line[i + 1 :].lstrip())
        i = line.find("::")
        if i == -1:
            return
        l1 = line[:i].rstrip()
        l2 = line[i + 2 :].lstrip()
        if not l1 or not l2:
            return
        if kind_selector:
            kind_selector = Kind_Selector(kind_selector)
        return kind_selector, Type_Param_Attr_Spec(l1), Type_Param_Decl_List(l2)

    def tostr(self):
        s = "INTEGER"
        if self.items[0] is not None:
            s += "%s, %s :: %s" % tuple(self.items)
        else:
            s += ", %s :: %s" % tuple(self.items[1:])
        return s
