from fparser.two.utils import (
    Base,
)

from name import Result_Name
from proc_language_binding_spec import Proc_Language_Binding_Spec

class Suffix(Base):  # R1229
    """
    ::

        <suffix> = <proc-language-binding-spec> [ RESULT ( <result-name> ) ]
                   | RESULT ( <result-name> ) [ <proc-language-binding-spec> ]
    """

    subclass_names = ["Proc_Language_Binding_Spec"]
    use_names = ["Result_Name"]

    @staticmethod
    def match(string):
        if string[:6].upper() == "RESULT":
            line = string[6:].lstrip()
            if not line.startswith("("):
                return
            i = line.find(")")
            if i == -1:
                return
            name = line[1:i].strip()
            if not name:
                return
            line = line[i + 1 :].lstrip()
            if line:
                return Result_Name(name), Proc_Language_Binding_Spec(line)
            return Result_Name(name), None
        if not string.endswith(")"):
            return
        i = string.rfind("(")
        if i == -1:
            return
        name = string[i + 1 : -1].strip()
        if not name:
            return
        line = string[:i].rstrip()
        if line[-6:].upper() != "RESULT":
            return
        line = line[:-6].rstrip()
        if not line:
            return
        return Result_Name(name), Proc_Language_Binding_Spec(line)

    def tostr(self):
        if self.items[1] is None:
            return "RESULT(%s)" % (self.items[0])
        return "RESULT(%s) %s" % self.items
