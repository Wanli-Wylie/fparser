from format import Format
from input_item import Input_Item_List
from io_control_spec_list import Io_Control_Spec_List
from output_item import Output_Item_List

class Read_Stmt(StmtBase):  # R910
    """
    Fortran2003 Rule R910::

        <read-stmt> = READ ( <io-control-spec-list> ) [ <input-item-list> ]
                        | READ <format> [ , <input-item-list> ]

    Attributes::

        items : (Io_Control_Spec_List, Format, Input_Item_List)

    """

    subclass_names = []
    use_names = ["Io_Control_Spec_List", "Input_Item_List", "Format"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "READ":
            return
        line = string[4:].lstrip()
        if line.startswith("("):
            line, repmap = string_replace_map(line)
            idx = line.find(")")
            if idx == -1:
                return
            trimline = line[1:idx].strip()
            if not trimline:
                return
            if idx == len(line) - 1:
                return Io_Control_Spec_List(repmap(trimline)), None, None
            return (
                Io_Control_Spec_List(repmap(trimline)),
                None,
                Input_Item_List(repmap(line[idx + 1 :].lstrip())),
            )
        if not line:
            return
        char = line[0].upper()
        # No parentheses therefore first argument must be a format
        # specifier (either a string or a line/label number
        if "A" <= char <= "Z" or char == "_":
            return
        line, repmap = string_replace_map(line.lstrip())
        # There must be a comma betwee the format specifier and the following
        # list of values/variables
        idx = line.find(",")
        if idx == -1:
            return None
        trimline = repmap(line[idx + 1 :].lstrip())
        if not trimline:
            return
        return (None, Format(repmap(line[:idx].rstrip())), Output_Item_List(trimline))

    def tostr(self):
        if self.items[0] is not None:
            assert self.items[1] is None, repr(self.items)
            if self.items[2] is None:
                return "READ(%s)" % (self.items[0])
            return "READ(%s) %s" % (self.items[0], self.items[2])
        assert self.items[1] is not None, repr(self.items)
        if self.items[2] is None:
            return "READ %s" % (self.items[1])
        return "READ %s, %s" % (self.items[1], self.items[2])
