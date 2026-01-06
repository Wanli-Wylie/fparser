from dummy_arg_name import Dummy_Arg_Name_List
from intent_spec import Intent_Spec

class Intent_Stmt(StmtBase):  # R536
    """
    ::

        <intent-stmt> = INTENT ( <intent-spec> ) [ :: ] <dummy-arg-name-list>

    """

    subclass_names = []
    use_names = ["Intent_Spec", "Dummy_Arg_Name_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "INTENT":
            return
        line = string[6:].lstrip()
        if not line or not line.startswith("("):
            return
        i = line.rfind(")")
        if i == -1:
            return
        spec = line[1:i].strip()
        if not spec:
            return
        line = line[i + 1 :].lstrip()
        if line.startswith("::"):
            line = line[2:].lstrip()
        if not line:
            return
        return Intent_Spec(spec), Dummy_Arg_Name_List(line)

    def tostr(self):
        return "INTENT(%s) :: %s" % self.items
