class Io_Implied_Do_Control(Base):  # R919
    """
    ::

        <io-implied-do-control> = <do-variable> = <scalar-int-expr> ,
            <scalar-int-expr> [ , <scalar-int-expr> ]

    """

    subclass_names = []
    use_names = ["Do_Variable", "Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        if "=" not in line:
            return
        v, exprs = line.split("=", 1)
        v = Do_Variable(repmap(v.rstrip()))
        exprs = exprs.lstrip().split(",")
        if len(exprs) not in [2, 3]:
            return
        exprs = tuple([Scalar_Int_Expr(repmap(e.strip())) for e in exprs])
        if len(exprs) == 2:
            return (v,) + exprs + (None,)
        return (v,) + exprs

    def tostr(self):
        if self.items[3] is not None:
            return "%s = %s, %s, %s" % (self.items)
        return "%s = %s, %s" % (self.items[:-1])
