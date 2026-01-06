from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)

from data_i_do_object import Data_I_Do_Object_List
from data_i_do_variable import Data_I_Do_Variable
from int_expr import Scalar_Int_Expr

class Data_Implied_Do(Base):  # R527
    """
    Fortran 2003 Rule R527::

        <data-implied-do> = ( <data-i-do-object-list> ,
            <data-i-do-variable> = <scalar-int-expr > ,
            <scalar-int-expr> [ , <scalar-int-expr> ] )

    """

    subclass_names = []
    use_names = ["Data_I_Do_Object_List", "Data_I_Do_Variable", "Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        if not (string.startswith("(") and string.endswith(")")):
            return
        line, repmap = string_replace_map(string[1:-1].strip())
        s = line.split("=", 1)
        if len(s) != 2:
            return
        lhs = s[0].rstrip()
        rhs = s[1].lstrip()
        s1 = lhs.rsplit(",", 1)
        if len(s1) != 2:
            return
        s2 = rhs.split(",")
        if len(s2) not in [2, 3]:
            return
        data_i_do_object_list = Data_I_Do_Object_List(repmap(s1[0].rstrip()))
        data_i_do_variable = Data_I_Do_Variable(repmap(s1[1].lstrip()))
        scalar_int_expr1 = Scalar_Int_Expr(repmap(s2[0].rstrip()))
        scalar_int_expr2 = Scalar_Int_Expr(repmap(s2[1].strip()))
        if len(s2) == 3:
            scalar_int_expr3 = Scalar_Int_Expr(repmap(s2[2].lstrip()))
        else:
            scalar_int_expr3 = None
        return (
            data_i_do_object_list,
            data_i_do_variable,
            scalar_int_expr1,
            scalar_int_expr2,
            scalar_int_expr3,
        )

    data_i_do_object_list = property(lambda self: self.items[0])
    data_i_do_variable = property(lambda self: self.items[1])
    scalar_int_expr1 = property(lambda self: self.items[2])
    scalar_int_expr2 = property(lambda self: self.items[3])
    scalar_int_expr3 = property(lambda self: self.items[4])

    def tostr(self):
        tmp = "%s, %s = %s, %s" % tuple(self.items[:4])
        if self.items[4] is not None:
            tmp += ", %s" % (self.items[4])
        return "(" + tmp + ")"
