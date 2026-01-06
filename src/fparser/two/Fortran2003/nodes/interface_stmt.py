class Interface_Stmt(StmtBase):  # R1203
    """
    ::

        <interface-stmt> = INTERFACE [ <generic-spec> ]
                           | ABSTRACT INTERFACE

    Attributes::

        items : ({Generic_Spec, 'ABSTRACT'},)

    """

    subclass_names = []
    use_names = ["Generic_Spec"]

    @staticmethod
    def match(string):
        if string[:9].upper() == "INTERFACE":
            line = string[9:].strip()
            if not line:
                return (None,)
            return (Generic_Spec(line),)
        if string[:8].upper() == "ABSTRACT":
            line = string[8:].strip()
            if line.upper() == "INTERFACE":
                return ("ABSTRACT",)

    def tostr(self):
        if self.items[0] == "ABSTRACT":
            return "ABSTRACT INTERFACE"
        if self.items[0] is None:
            return "INTERFACE"
        return "INTERFACE %s" % (self.items[0])
