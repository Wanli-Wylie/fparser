from dummy_arg import Dummy_Arg_List
from name import Entry_Name
from suffix import Suffix

class Entry_Stmt(StmtBase):  # R1235
    """
    ::

        <entry-stmt> = ENTRY <entry-name> [ ( [ <dummy-arg-list> ] ) [ <suffix> ] ]

    Attributes::

        items : (Entry_Name, Dummy_Arg_List, Suffix)

    """

    subclass_names = []
    use_names = ["Entry_Name", "Dummy_Arg_List", "Suffix"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "ENTRY":
            return
        line = string[5:].lstrip()
        i = line.find("(")
        if i == -1:
            return Entry_Name(line), None, None
        name = Entry_Name(line[:i].rstrip())
        line, repmap = string_replace_map(line[i:])
        i = line.find(")")
        if i == -1:
            return
        args = line[1:i].strip()
        args = Dummy_Arg_List(repmap(args)) if args else None
        line = line[i + 1 :].lstrip()
        if line:
            return name, args, Suffix(repmap(line))
        return name, args, None

    def tostr(self):
        name, args, suffix = self.items
        if suffix is None:
            if args is None:
                return "ENTRY %s()" % (name)
            return "ENTRY %s(%s)" % (name, args)
        elif args is None:
            return "ENTRY %s() %s" % (name, suffix)
        return "ENTRY %s(%s) %s" % (name, args, suffix)
