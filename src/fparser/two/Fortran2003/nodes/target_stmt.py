from target_entity_decl import Target_Entity_Decl_List

class Target_Stmt(StmtBase):  # R546
    """
    ::

        <target-stmt> = TARGET [ :: ] <target-entity-decl-list>

    """

    subclass_names = []
    use_names = ["Target_Entity_Decl_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "TARGET":
            return
        line = string[6:].lstrip()
        if line.startswith("::"):
            line = line[2:].lstrip()
        return (Target_Entity_Decl_List(line),)

    def tostr(self):
        return "TARGET :: %s" % (self.items[0])
