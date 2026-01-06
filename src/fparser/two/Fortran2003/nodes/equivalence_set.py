class Equivalence_Set(Base):  # R555
    """
    ::

        <equivalence-set> = ( <equivalence-object> , <equivalence-object-list> )

    """

    subclass_names = []
    use_names = ["Equivalence_Object", "Equivalence_Object_List"]

    @staticmethod
    def match(string):
        if not string or string[0] + string[-1] != "()":
            return
        line = string[1:-1].strip()
        if not line:
            return
        tmp = Equivalence_Object_List(line)
        obj = tmp.items[0]
        tmp.items = tmp.items[1:]
        if not tmp.items:
            return
        return obj, tmp

    def tostr(self):
        return "(%s, %s)" % tuple(self.items)
