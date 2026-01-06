class Goto_Stmt(StmtBase):  # R845
    """
    <goto-stmt> = GO TO <label>
    """

    subclass_names = []
    use_names = ["Label"]

    @staticmethod
    def match(string):
        if string[:2].upper() != "GO":
            return
        line = string[2:].lstrip()
        if line[:2].upper() != "TO":
            return
        return (Label(line[2:].lstrip()),)

    def tostr(self):
        return "GO TO %s" % (self.items[0])
