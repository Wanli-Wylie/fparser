from fparser.two.utils import (
    StmtBase,
)

from mask_expr import Mask_Expr

class Where_Construct_Stmt(StmtBase):  # R745
    """
    ::

        <where-construct-stmt> = [ <where-construct-name> : ] WHERE ( <mask-expr> )

    """

    subclass_names = []
    use_names = ["Where_Construct_Name", "Mask_Expr"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "WHERE":
            return
        line = string[5:].lstrip()
        if not line:
            return
        if line[0] + line[-1] != "()":
            return
        line = line[1:-1].strip()
        if not line:
            return
        return (Mask_Expr(line),)

    def tostr(self):
        return "WHERE (%s)" % tuple(self.items)

    def get_start_name(self):
        return self.item.name
