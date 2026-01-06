from elsewhere_stmt import Elsewhere_Stmt
from mask_expr import Mask_Expr
from name import Where_Construct_Name

class Masked_Elsewhere_Stmt(StmtBase):  # R749
    """
    ::

        <masked-elsewhere-stmt> = ELSEWHERE
                                  ( <mask-expr> ) [ <where-construct-name> ]

    """

    import re

    subclass_names = []
    use_names = ["Mask_Expr", "Where_Construct_Name"]

    @staticmethod
    def match(string):
        if not Elsewhere_Stmt._regex.match(string):
            return
        idx = string.upper().index("WHERE")
        line = string[idx + 5 :].lstrip()

        if not line.startswith("("):
            return
        i = line.rfind(")")
        if i == -1:
            return
        expr = line[1:i].strip()
        if not expr:
            return
        line = line[i + 1 :].rstrip()
        if line:
            return Mask_Expr(expr), Where_Construct_Name(line)
        return Mask_Expr(expr), None

    def tostr(self):
        if self.items[1] is None:
            return "ELSEWHERE(%s)" % (self.items[0])
        return "ELSEWHERE(%s) %s" % self.items

    def get_end_name(self):
        """
        :return: the name at the END of this block, if it exists
        :rtype: str or NoneType
        """
        name = self.items[1]
        if name is not None:
            return name.string
        return None
