class Initialization(Base):  # R506
    """
    ::

        <initialization> =  = <initialization-expr>
                           | => <null-init>

    """

    subclass_names = []
    use_names = ["Initialization_Expr", "Null_Init"]

    @staticmethod
    def match(string):
        if string.startswith("=>"):
            return "=>", Null_Init(string[2:].lstrip())
        if string.startswith("="):
            return "=", Initialization_Expr(string[1:].lstrip())
        return None

    def tostr(self):
        return "%s %s" % self.items
