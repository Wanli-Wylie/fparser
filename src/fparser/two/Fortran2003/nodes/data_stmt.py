from data_stmt_set import Data_Stmt_Set

class Data_Stmt(StmtBase):  # R524
    """
    Fortran 2003 Rule R524::

        <data-stmt> = DATA <data-stmt-set> [ [ , ] <data-stmt-set> ]...

    """

    subclass_names = []
    use_names = ["Data_Stmt_Set"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "DATA":
            return
        line, repmap = string_replace_map(string[4:].lstrip())
        i = line.find("/")
        if i == -1:
            return
        i = line.find("/", i + 1)
        if i == -1:
            return
        items = [Data_Stmt_Set(repmap(line[: i + 1]))]
        line = line[i + 1 :].lstrip()
        while line:
            if line.startswith(","):
                line = line[1:].lstrip()
            i = line.find("/")
            if i == -1:
                return
            i = line.find("/", i + 1)
            if i == -1:
                return
            items.append(Data_Stmt_Set(repmap(line[: i + 1])))
            line = line[i + 1 :].lstrip()
        return tuple(items)

    def tostr(self):
        return "DATA " + ", ".join(map(str, self.items))
