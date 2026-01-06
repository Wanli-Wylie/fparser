class Dealloc_Opt(KeywordValueBase):  # R636
    """
    ::

        <dealloc-opt> = STAT = <stat-variable>
                        | ERRMSG = <errmsg-variable>

    """

    subclass_names = []
    use_names = ["Stat_Variable", "Errmsg_Variable"]

    @staticmethod
    def match(string):
        for k, v in [("STAT", Stat_Variable), ("ERRMSG", Errmsg_Variable)]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None
