from fparser.two.utils import (
    StmtBase,
)

from name import Block_Data_Name

class Block_Data_Stmt(StmtBase):  # R1117
    """
    ::

        <block-data-stmt> = BLOCK DATA [ <block-data-name> ]

    """

    subclass_names = []
    use_names = ["Block_Data_Name"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "BLOCK":
            return
        line = string[5:].lstrip()
        if line[:4].upper() != "DATA":
            return
        line = line[4:].lstrip()
        if not line:
            return (None,)
        return (Block_Data_Name(line),)

    def tostr(self):
        if self.items[0] is None:
            return "BLOCK DATA"
        return "BLOCK DATA %s" % self.items

    def get_name(self):
        return self.items[0]
