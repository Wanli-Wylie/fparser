class Pointer_Assignment_Stmt(StmtBase):  # R735
    """
    ::

        <pointer-assignment-stmt> = <data-pointer-object> [
            ( <bounds-spec-list> ) ] => <data-target>
            | <data-pointer-object> ( <bounds-remapping-list> ) => <data-target>
            | <proc-pointer-object> => <proc-target>

    """

    subclass_names = []
    use_names = [
        "Data_Pointer_Object",
        "Bounds_Spec_List",
        "Data_Target",
        "Bounds_Remapping_List",
        "Proc_Pointer_Object",
        "Proc_Target",
    ]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        i = line.find("=>")
        if i == -1:
            return
        lhs = line[:i].rstrip()
        rhs = repmap(line[i + 2 :].lstrip())
        if lhs.endswith(")"):
            i = lhs.rfind("(")
            if i == -1:
                return
            o = repmap(lhs[:i].rstrip())
            tmp = repmap(lhs[i + 1 : -1].strip())
            try:
                return Data_Pointer_Object(o), Bounds_Spec_List(tmp), Data_Target(rhs)
            except NoMatchError as msg:
                return (
                    Data_Pointer_Object(o),
                    Bounds_Remapping_List(tmp),
                    Data_Target(rhs),
                )
        else:
            lhs = repmap(lhs)
        try:
            return Data_Pointer_Object(lhs), None, Data_Target(rhs)
        except NoMatchError as msg:
            return Proc_Pointer_Object(lhs), None, Proc_Target(rhs)

    def tostr(self):
        if self.items[1] is None:
            return "%s => %s" % (self.items[0], self.items[2])
        return "%s(%s) => %s" % (self.items)
