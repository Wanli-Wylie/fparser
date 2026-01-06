from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)

from data_stmt_object import Data_Stmt_Object_List
from data_stmt_value import Data_Stmt_Value_List

class Data_Stmt_Set(Base):  # R525
    """
    Fortran2003 Rule R525::

        <data-stmt-set> = <data-stmt-object-list> / <data-stmt-value-list> /

    """

    subclass_names = []
    use_names = ["Data_Stmt_Object_List", "Data_Stmt_Value_List"]

    @staticmethod
    def match(string):
        if not string.endswith("/"):
            return
        line, repmap = string_replace_map(string)
        i = line.find("/")
        if i == -1:
            return
        data_stmt_object_list = Data_Stmt_Object_List(repmap(line[:i].rstrip()))
        data_stmt_value_list = Data_Stmt_Value_List(repmap(line[i + 1 : -1].strip()))
        return data_stmt_object_list, data_stmt_value_list

    data_stmt_object_list = property(lambda self: self.items[0])
    data_stmt_value_list = property(lambda self: self.items[1])

    def tostr(self):
        return "%s / %s /" % tuple(self.items)
