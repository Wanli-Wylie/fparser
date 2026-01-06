from mask_expr import Mask_Expr
from where_assignment_stmt import Where_Assignment_Stmt

class Where_Stmt(StmtBase):  # R743
    """
    ::

        <where-stmt> = WHERE ( <mask-expr> ) <where-assignment-stmt>

    """

    subclass_names = []
    use_names = ["Mask_Expr", "Where_Assignment_Stmt"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "WHERE":
            return
        line, repmap = string_replace_map(string[5:].lstrip())
        if not line.startswith("("):
            return
        i = line.find(")")
        if i == -1:
            return
        stmt = repmap(line[i + 1 :].lstrip())
        if not stmt:
            return
        expr = repmap(line[1:i].strip())
        if not expr:
            return
        return Mask_Expr(expr), Where_Assignment_Stmt(stmt)

    def tostr(self):
        return "WHERE (%s) %s" % tuple(self.items)
