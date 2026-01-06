from name import Procedure_Name_List

class Procedure_Stmt(StmtBase):  # R1206
    """
    ::

        <procedure-stmt> = [ MODULE ] PROCEDURE <procedure-name-list>

    Attributes::

        items : (Procedure_Name_List, )

    """

    subclass_names = []
    use_names = ["Procedure_Name_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() == "MODULE":
            line = string[6:].lstrip()
        else:
            line = string
        if line[:9].upper() != "PROCEDURE":
            return
        line = line[9:].lstrip()
        return (Procedure_Name_List(line),)

    def tostr(self):
        return "MODULE PROCEDURE %s" % (self.items[0])
