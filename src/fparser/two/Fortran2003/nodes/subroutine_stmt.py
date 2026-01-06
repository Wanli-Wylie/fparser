from dummy_arg import Dummy_Arg_List
from name import Subroutine_Name
from prefix import Prefix
from proc_language_binding_spec import Proc_Language_Binding_Spec

class Subroutine_Stmt(StmtBase, ScopingRegionMixin):  # R1232
    """
    Fortran2003 rule R1232::

        subroutine-stmt is [ prefix ] SUBROUTINE subroutine-name \
[ ( [ dummy-arg-list ] ) [ proc-language-binding-spec ] ]

    C1242 (R1227) A prefix shall not specify ELEMENTAL if
    proc-language-binding-spec appears in the function-stmt or
    subroutine-stmt. The spec associates this constraint with R1227
    but it needs to be checked here.

    """

    subclass_names = []
    use_names = [
        "Prefix",
        "Subroutine_Name",
        "Dummy_Arg_List",
        "Proc_Language_Binding_Spec",
    ]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        m = pattern.subroutine.search(line)
        if m is None:
            return
        prefix = line[: m.start()].rstrip() or None
        if prefix is not None:
            prefix = Prefix(repmap(prefix))
        line = line[m.end() :].lstrip()
        m = pattern.name.match(line)
        if m is None:
            return
        name = Subroutine_Name(m.group())
        line = line[m.end() :].lstrip()
        dummy_args = None
        if line.startswith("("):
            i = line.find(")")
            if i == -1:
                return
            dummy_args = line[1:i].strip() or None
            if dummy_args is not None:
                dummy_args = Dummy_Arg_List(repmap(dummy_args))
            line = line[i + 1 :].lstrip()
        binding_spec = None
        if line:
            binding_spec = Proc_Language_Binding_Spec(repmap(line))
        if not c1242_valid(prefix, binding_spec):
            return None
        return prefix, name, dummy_args, binding_spec

    def get_name(self):
        return self.items[1]

    def tostr(self):
        if self.items[0] is not None:
            s = "%s SUBROUTINE %s" % (self.items[0], self.items[1])
        else:
            s = "SUBROUTINE %s" % (self.items[1])
        if self.items[2] is not None:
            s += "(%s)" % (self.items[2])
        if self.items[3] is not None:
            s += " %s" % (self.items[3])
        return s
