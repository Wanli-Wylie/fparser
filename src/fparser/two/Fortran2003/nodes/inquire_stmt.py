class Inquire_Stmt(StmtBase):  # R929
    """
    Fortran2003 Rule R929::

        <inquire-stmt> = INQUIRE ( <inquire-spec-list> )
                         | INQUIRE ( IOLENGTH = <scalar-int-variable> )
                           <output-item-list>

    Attributes::

        items : (Inquire_Spec_List, Scalar_Int_Variable, Output_Item_List)

    """

    subclass_names = []
    use_names = ["Inquire_Spec_List", "Scalar_Int_Variable", "Output_Item_List"]

    @staticmethod
    def match(string):
        if string[:7].upper() != "INQUIRE":
            return
        line = string[7:].lstrip()
        if not line.startswith("("):
            return
        if line.endswith(")"):
            return Inquire_Spec_List(line[1:-1].strip()), None, None
        line, repmap = string_replace_map(line)
        i = line.find(")")
        if i == -1:
            return
        tmp = repmap(line[1:i])
        if tmp[:8].upper() != "IOLENGTH":
            return
        tmp = tmp[8:].lstrip()
        if not tmp.startswith("="):
            return
        tmp = tmp[1:].lstrip()
        return (
            None,
            Scalar_Int_Variable(tmp),
            Output_Item_List(repmap(line[i + 1 :].lstrip())),
        )

    def tostr(self):
        if self.items[0] is None:
            assert None not in self.items[1:], repr(self.items)
            return "INQUIRE(IOLENGTH=%s) %s" % (self.items[1:])
        return "INQUIRE(%s)" % (self.items[0])
