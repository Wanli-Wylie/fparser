class Length_Selector(Base):  # R425
    """
    ::

        <length -selector> = ( [ LEN = ] <type-param-value> )
                            | * <char-length> [ , ]
    """

    subclass_names = []
    use_names = ["Type_Param_Value", "Char_Length"]

    @staticmethod
    def match(string):
        if string[0] + string[-1] == "()":
            line = string[1:-1].strip()
            if line[:3].upper() == "LEN" and line[3:].lstrip().startswith("="):
                line = line[3:].lstrip()
                line = line[1:].lstrip()
            return "(", Type_Param_Value(line), ")"
        if not string.startswith("*"):
            return
        line = string[1:].lstrip()
        if string[-1] == ",":
            line = line[:-1].rstrip()
        return "*", Char_Length(line)

    def tostr(self):
        if len(self.items) == 2:
            return "%s%s" % tuple(self.items)
        return "%sLEN = %s%s" % tuple(self.items)
