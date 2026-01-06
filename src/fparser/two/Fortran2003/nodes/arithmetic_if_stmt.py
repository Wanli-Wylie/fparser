from fparser.two.utils import (
    StmtBase,
)

from label import Label
from numeric_expr import Scalar_Numeric_Expr

class Arithmetic_If_Stmt(StmtBase):  # R847
    """
    ::

        <arithmetic-if-stmt> = IF ( <scalar-numeric-expr> ) <label> ,
            <label> , <label>

    """

    subclass_names = []
    use_names = ["Scalar_Numeric_Expr", "Label"]

    @staticmethod
    def match(string):
        if string[:2].upper() != "IF":
            return
        line = string[2:].lstrip()
        if not line.startswith("("):
            return
        i = line.rfind(")")
        if i == -1:
            return
        labels = line[i + 1 :].lstrip().split(",")
        if len(labels) != 3:
            return
        labels = [Label(l.strip()) for l in labels]
        return (Scalar_Numeric_Expr(line[1:i].strip()),) + tuple(labels)

    def tostr(self):
        return "IF (%s) %s, %s, %s" % self.items
