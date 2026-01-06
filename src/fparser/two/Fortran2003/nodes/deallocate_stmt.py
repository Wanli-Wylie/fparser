class Deallocate_Stmt(StmtBase):  # R635
    """
    ::

        <deallocate-stmt> = DEALLOCATE ( <allocate-object-list> [
            , <dealloc-opt-list> ] )

    """

    subclass_names = []
    use_names = ["Allocate_Object_List", "Dealloc_Opt_List"]

    @staticmethod
    def match(string):
        if string[:10].upper() != "DEALLOCATE":
            return
        line = string[10:].lstrip()
        if not line or line[0] != "(" or line[-1] != ")":
            return
        line, repmap = string_replace_map(line[1:-1].strip())
        i = line.find("=")
        opts = None
        if i != -1:
            j = line[:i].rfind(",")
            assert j != -1, repr((i, j, line))
            opts = Dealloc_Opt_List(repmap(line[j + 1 :].lstrip()))
            line = line[:j].rstrip()
        return Allocate_Object_List(repmap(line)), opts

    def tostr(self):
        if self.items[1] is not None:
            return "DEALLOCATE(%s, %s)" % (self.items)
        return "DEALLOCATE(%s)" % (self.items[0])
