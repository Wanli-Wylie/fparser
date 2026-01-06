class Generic_Spec(Base):  # R1207
    """
    ::

        <generic-spec> = <generic-name>
                         | OPERATOR ( <defined-operator> )
                         | ASSIGNMENT ( = )
                         | <dtio-generic-spec>
    Attributes::

        items : ({'OPERATOR', 'ASSIGNMENT'}, {Defined_Operator, '='})

    """

    subclass_names = ["Generic_Name", "Dtio_Generic_Spec"]
    use_names = ["Defined_Operator"]

    @staticmethod
    def match(string):
        if string[:8].upper() == "OPERATOR":
            line = string[8:].lstrip()
            if not line or line[0] != "(" or line[-1] != ")":
                return
            return "OPERATOR", Defined_Operator(line[1:-1].strip())
        if string[:10].upper() == "ASSIGNMENT":
            line = string[10:].lstrip()
            if not line or line[0] != "(" or line[-1] != ")":
                return
            if line[1:-1].strip() == "=":
                return "ASSIGNMENT", "="

    def tostr(self):
        return "%s(%s)" % (self.items)
