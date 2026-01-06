class Flush_Stmt(StmtBase):  # R927
    """
    Fortran2003 Rule R927::

        <flush-stmt> = FLUSH <file-unit-number>
                        | FLUSH ( <position-spec-list> )

    Attributes::

        items : (File_Unit_Number, Position_Spec_List)

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Position_Spec_List"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "FLUSH":
            return
        line = string[5:].lstrip()
        if line.startswith("("):
            if not line.endswith(")"):
                return
            return None, Position_Spec_List(line[1:-1].strip())
        return File_Unit_Number(line), None

    def tostr(self):
        if self.items[0] is not None:
            assert self.items[1] is None, repr(self.items)
            return "FLUSH %s" % (self.items[0])
        return "FLUSH(%s)" % (self.items[1])
