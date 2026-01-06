class Else_If_Stmt(StmtBase):  # R804
    """
    ::

        <else-if-stmt> = ELSE IF ( <scalar-logical-expr> ) THEN
            [ <if-construct-name> ]

    """

    subclass_names = []
    use_names = ["Scalar_Logical_Expr", "If_Construct_Name"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "ELSE":
            return
        line = string[4:].lstrip()
        if line[:2].upper() != "IF":
            return
        line = line[2:].lstrip()
        if not line.startswith("("):
            return
        i = line.rfind(")")
        if i == -1:
            return
        expr = line[1:i].strip()
        line = line[i + 1 :].lstrip()
        if line[:4].upper() != "THEN":
            return
        line = line[4:].lstrip()
        if line:
            return Scalar_Logical_Expr(expr), If_Construct_Name(line)
        return Scalar_Logical_Expr(expr), None

    def tostr(self):
        if self.items[1] is None:
            return "ELSE IF (%s) THEN" % (self.items[0])
        return "ELSE IF (%s) THEN %s" % self.items

    def get_end_name(self):
        """
        :return: the name at the END of this block, if it exists
        :rtype: str or NoneType
        """
        name = self.items[1]
        if name is not None:
            return name.string
        return None
