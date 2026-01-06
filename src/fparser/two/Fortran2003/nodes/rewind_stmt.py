from file_unit_number import File_Unit_Number
from position_spec import Position_Spec_List

class Rewind_Stmt(StmtBase):  # R925
    """
    Fortran2003 Rule R925::

        <rewind-stmt> = REWIND <file-unit-number>
                        | REWIND ( <position-spec-list> )

    Attributes::

        items : (File_Unit_Number, Position_Spec_List)

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Position_Spec_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "REWIND":
            return
        line = string[6:].lstrip()
        if line.startswith("("):
            if not line.endswith(")"):
                return
            return None, Position_Spec_List(line[1:-1].strip())
        return File_Unit_Number(line), None

    def tostr(self):
        if self.items[0] is not None:
            assert self.items[1] is None, repr(self.items)
            return "REWIND %s" % (self.items[0])
        return "REWIND(%s)" % (self.items[1])
