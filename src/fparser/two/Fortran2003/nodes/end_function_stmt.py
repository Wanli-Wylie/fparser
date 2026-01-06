from fparser.two.utils import (
    EndStmtBase,
)

from name import Function_Name

class End_Function_Stmt(EndStmtBase):  # R1230
    """
    <end-function-stmt> = END [ FUNCTION [ <function-name> ] ]
    """

    subclass_names = []
    use_names = ["Function_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("FUNCTION", Function_Name, string)
