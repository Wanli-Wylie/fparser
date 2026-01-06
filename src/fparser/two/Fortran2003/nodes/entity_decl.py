from array_spec import Array_Spec
from char_length import Char_Length
from initialization import Initialization
from name import Name

class Entity_Decl(Base):  # R504
    """
    ::

        <entity-decl> = <object-name> [ ( <array-spec> ) ]
            [ * <char-length> ] [ <initialization> ]
                        | <function-name> [ * <char-length> ]

    """

    subclass_names = []
    use_names = [
        "Object_Name",
        "Array_Spec",
        "Char_Length",
        "Initialization",
        "Function_Name",
    ]

    @staticmethod
    def match(string, target=False):
        m = pattern.name.match(string)
        if m is None:
            return
        name = Name(m.group())
        newline = string[m.end() :].lstrip()
        if not newline:
            return name, None, None, None
        array_spec = None
        char_length = None
        init = None
        if newline.startswith("("):
            line, repmap = string_replace_map(newline)
            i = line.find(")")
            if i == -1:
                return
            array_spec = Array_Spec(repmap(line[1:i].strip()))
            newline = repmap(line[i + 1 :].lstrip())
        if target:
            if newline:
                return
            return name, array_spec, None, None
        if newline.startswith("*"):
            line, repmap = string_replace_map(newline)
            i = line.find("=")
            if i != -1:
                char_length = repmap(line[1:i].strip())
                newline = repmap(newline[i:].lstrip())
            else:
                char_length = repmap(newline[1:].strip())
                newline = ""
            char_length = Char_Length(char_length)
        if newline.startswith("="):
            init = Initialization(newline)
        elif newline:
            return
        else:
            assert newline == "", repr((newline, string))
        return name, array_spec, char_length, init

    def tostr(self):
        s = str(self.items[0])
        if self.items[1] is not None:
            s += "(" + str(self.items[1]) + ")"
        if self.items[2] is not None:
            s += "*" + str(self.items[2])
        if self.items[3] is not None:
            s += " " + str(self.items[3])
        return s

    def get_name(self):
        """Provides the entity name as an instance of the :py:class:`Name` class.

        :rtype: :py:class:`Name`
        """
        return self.items[0]


class Entity_Decl_List(SequenceBase):
    subclass_names = ["Entity_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Entity_Decl, string)

    def __iter__(self):
        return iter(self.items)
