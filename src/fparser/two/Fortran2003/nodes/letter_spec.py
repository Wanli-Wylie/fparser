from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Letter_Spec(Base):  # R551
    """
    ::

        <letter-spec> = <letter> [ - <letter> ]

    """

    subclass_names = []

    @staticmethod
    def match(string):
        if len(string) == 1:
            lhs = string.upper()
            if "A" <= lhs <= "Z":
                return lhs, None
            return
        if "-" not in string:
            return
        lhs, rhs = string.split("-", 1)
        lhs = lhs.strip().upper()
        rhs = rhs.strip().upper()
        if not len(lhs) == len(rhs) == 1:
            return
        if not ("A" <= lhs <= rhs <= "Z"):
            return
        return lhs, rhs

    def tostr(self):
        if self.items[1] is None:
            return str(self.items[0])
        return "%s - %s" % tuple(self.items)


class Letter_Spec_List(SequenceBase):
    subclass_names = ["Letter_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Letter_Spec, string)

    def __iter__(self):
        return iter(self.items)
