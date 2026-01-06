from name import Parent_Type_Name

class Type_Attr_Spec(Base):  # R431
    """
    ::

        <type-attr-spec> = <access-spec>
                           | EXTENDS ( <parent-type-name> )
                           | ABSTRACT
                           | BIND (C)

    """

    subclass_names = ["Access_Spec", "Language_Binding_Spec"][:-1]
    use_names = ["Parent_Type_Name"]

    @staticmethod
    def match(string):
        if len(string) == 8 and string.upper() == "ABSTRACT":
            return "ABSTRACT", None
        if string[:4].upper() == "BIND":
            line = string[4:].lstrip()
            if not line or line[0] + line[-1] != "()":
                return
            line = line[1:-1].strip()
            if line.upper() == "C":
                return "BIND", "C"
        elif string[:7].upper() == "EXTENDS":
            line = string[7:].lstrip()
            if not line or line[0] + line[-1] != "()":
                return
            return "EXTENDS", Parent_Type_Name(line[1:-1].strip())

    def tostr(self):
        if self.items[1] is None:
            return "%s" % (self.items[0])
        return "%s(%s)" % (self.items)


class Type_Attr_Spec_List(SequenceBase):
    subclass_names = ["Type_Attr_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)
