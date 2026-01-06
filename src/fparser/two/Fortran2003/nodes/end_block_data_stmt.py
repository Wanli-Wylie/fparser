from fparser.two.utils import (
    EndStmtBase,
)

from name import Block_Data_Name

class End_Block_Data_Stmt(EndStmtBase):  # R1118
    """
    ::

        <end-block-data-stmt> = END [ BLOCK DATA [ <block-data-name> ] ]

    """

    subclass_names = []
    use_names = ["Block_Data_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("BLOCK DATA", Block_Data_Name, string)
