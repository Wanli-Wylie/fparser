class Else_Stmt(StmtBase):  # R805
    """
    <else-stmt> = ELSE [ <if-construct-name> ]
    """

    subclass_names = []
    use_names = ["If_Construct_Name"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "ELSE":
            return
        line = string[4:].lstrip()
        if line:
            return (If_Construct_Name(line),)
        return (None,)

    def tostr(self):
        if self.items[0] is None:
            return "ELSE"
        return "ELSE %s" % self.items

    def get_end_name(self):
        """
        :return: the name at the END of this block, if it exists
        :rtype: str or NoneType
        """
        name = self.items[0]
        if name is not None:
            return name.string
        return None
