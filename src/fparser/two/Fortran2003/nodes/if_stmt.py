from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    StmtBase,
)

from action_stmt_c802 import Action_Stmt_C802
from logical_expr import Scalar_Logical_Expr

class If_Stmt(StmtBase):  # R807
    """
    Fortran 2003 rule R807::

        if-stmt is IF ( scalar-logical-expr ) action-stmt

    C802 (R807) The action-stmt in the if-stmt shall not be an if-stmt,
    end-program-stmt, end-function-stmt, or end-subroutine-stmt.

    """

    subclass_names = []
    use_names = ["Scalar_Logical_Expr", "Action_Stmt_C802"]
    action_stmt_cls = Action_Stmt_C802

    @classmethod
    def match(cls, string):
        """Implements the matching for an if statement that controls a single
        action statement

        This is implemented as a class method to allow parameterizing the
        type that is used to match the action-stmt. It is specified by the
        attribute :py:attr:`action_stmt_cls`, which can be overwritten in
        derived classes to specify an updated version, so done for example
        in the Fortran 2008 version :py:class:`fparser.two.Fortran2008.If_Stmt`.

        :param str string: Text that we are trying to match.

        :returns: None if there is no match or, if there is a match, a \
            2-tuple containing the logical expression as an object matched by \
            :py:class:`fparser.two.Fortran2003.Scalar_Logical_Expr` and the \
            action statement as an object matching ``cls.action_stmt_cls``. 
        :rtype: (:py:class:`fparser.two.Fortran2003.Scalar_Logical_Expr`,
            :py:class:`fparser.two.Fortran2003.Action_Stmt_C802`) \
            or NoneType

        """
        if string[:2].upper() != "IF":
            return
        line, repmap = string_replace_map(string)
        line = line[2:].lstrip()
        if not line.startswith("("):
            return
        i = line.find(")")
        if i == -1:
            return
        expr = repmap(line[1:i].strip())
        stmt = repmap(line[i + 1 :].lstrip())
        return Scalar_Logical_Expr(expr), cls.action_stmt_cls(stmt)

    def tostr(self):
        return "IF (%s) %s" % self.items
