from file_unit_number import File_Unit_Number
from position_spec import Position_Spec_List

class Backspace_Stmt(StmtBase):  # R923
    """
    Fortran2003 Rule R923::

        <backspace-stmt> = BACKSPACE <file-unit-number>
                           | BACKSPACE ( <position-spec-list> )

    Attributes::

        items : (File_Unit_Number, Position_Spec_List)

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Position_Spec_List"]

    @staticmethod
    def match(string):
        if string[:9].upper() != "BACKSPACE":
            return
        line = string[9:].lstrip()
        if line.startswith("("):
            if not line.endswith(")"):
                return
            return None, Position_Spec_List(line[1:-1].strip())
        return File_Unit_Number(line), None

    def tostr(self):
        if self.items[0] is not None:
            assert self.items[1] is None, repr(self.items)
            return "BACKSPACE %s" % (self.items[0])
        return "BACKSPACE(%s)" % (self.items[1])
