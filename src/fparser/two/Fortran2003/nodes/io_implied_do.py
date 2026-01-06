from io_implied_do_control import Io_Implied_Do_Control
from io_implied_do_object import Io_Implied_Do_Object_List

class Io_Implied_Do(Base):  # R917
    """
    ::

        <io-implied-do> = ( <io-implied-do-object-list> , <io-implied-do-control> )
    """

    subclass_names = []
    use_names = ["Io_Implied_Do_Object_List", "Io_Implied_Do_Control"]

    @staticmethod
    def match(string):
        if len(string) <= 9 or string[0] != "(" or string[-1] != ")":
            return
        line, repmap = string_replace_map(string[1:-1].strip())
        i = line.rfind("=")
        if i == -1:
            return
        j = line[:i].rfind(",")
        if j == -1:
            return
        return (
            Io_Implied_Do_Object_List(repmap(line[:j].rstrip())),
            Io_Implied_Do_Control(repmap(line[j + 1 :].lstrip())),
        )

    def tostr(self):
        return "(%s, %s)" % (self.items)
