class Alloc_Opt(KeywordValueBase):  # R624
    """
    ::

        <alloc-opt> = STAT = <stat-variable>
                      | ERRMSG = <errmsg-variable>
                      | SOURCE = <source-expr>

    """

    subclass_names = []
    use_names = ["Stat_Variable", "Errmsg_Variable", "Source_Expr"]
    #: The keywords tested for in the match() method.
    _keyword_pairs = [
        ("STAT", Stat_Variable),
        ("ERRMSG", Errmsg_Variable),
        ("SOURCE", Source_Expr),
    ]

    @classmethod
    def match(cls, string):
        for k, v in cls._keyword_pairs:
            obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            if obj is not None:
                return obj
        return None


class Alloc_Opt_List(SequenceBase):
    subclass_names = ["Alloc_Opt"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Alloc_Opt, string)

    def __iter__(self):
        return iter(self.items)
