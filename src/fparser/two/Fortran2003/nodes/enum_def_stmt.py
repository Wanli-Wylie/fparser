from fparser.two.utils import (
    StmtBase,
)

class Enum_Def_Stmt(StmtBase):  # R461
    """
    ::

        <enum-def-stmt> = ENUM, BIND(C)

    """

    subclass_names = []
    use_names = []

    @staticmethod
    def match(string):
        if string.upper().replace(" ", "") != "ENUM,BIND(C)":
            return
        return ("ENUM, BIND(C)",)

    def tostr(self):
        return "%s" % (self.items[0])
