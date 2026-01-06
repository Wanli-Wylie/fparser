from char_literal_constant import Char_Literal_Constant
from int_literal_constant import Int_Literal_Constant
from m import M
from v import V_List
from w import W

class Data_Edit_Desc(Base):  # R1005
    """
    ::

        <data-edit-desc> =   I <w> [ . <m> ]
                           | B <w> [ . <m> ]
                           | O <w> [ . <m> ]
                           | Z <w> [ . <m> ]
                           | L <w>
                           | A [ <w> ]
                           | DT [ <char-literal-constant> ] [ ( <v-list> ) ]
                           | <data-edit-desc-c1002>

    """

    subclass_names = ["Data_Edit_Desc_C1002"]
    use_names = ["W", "M", "Char_Literal_Constant", "V_List"]

    @staticmethod
    def match(string):
        c = string[0].upper()
        if c in ["I", "B", "O", "Z"]:
            line = string[1:].lstrip()
            if "." in line:
                i1, i2 = line.split(".", 1)
                i1 = i1.rstrip()
                i2 = i2.lstrip()
                return c, W(i1), M(i2), None, Int_Literal_Constant
            return c, W(line), None, None
        if c == "L":
            line = string[1:].lstrip()
            if not line:
                return
            return c, W(line), None, None
        if c == "A":
            line = string[1:].lstrip()
            if not line:
                return c, None, None, None
            return c, W(line), None, None
        c = string[:2].upper()
        if len(c) != 2:
            return
        if c == "DT":
            line = string[2:].lstrip()
            if not line:
                return c, None, None, None
            lst = None
            if line.endswith(")"):
                i = line.rfind("(")
                if i == -1:
                    return
                tmp = line[i + 1 : -1].strip()
                if not tmp:
                    return
                lst = V_List(tmp)
                line = line[:i].rstrip()
            if not line:
                return c, None, lst, None
            return c, Char_Literal_Constant(line), lst, None
        return None

    def tostr(self):
        c = self.items[0]
        if c in ["I", "B", "O", "Z", "A", "L"]:
            if self.items[2] is None:
                if self.items[1] is None:
                    return c
                return "%s%s" % (c, self.items[1])
            return "%s%s.%s" % (c, self.items[1], self.items[2])
        if c == "DT":
            if self.items[1] is None:
                if self.items[2] is None:
                    return c
                else:
                    return "%s(%s)" % (c, self.items[2])
            else:
                if self.items[2] is None:
                    return "%s%s" % (c, self.items[1])
                else:
                    return "%s%s(%s)" % (c, self.items[1], self.items[2])
        raise NotImplementedError(repr(c))
