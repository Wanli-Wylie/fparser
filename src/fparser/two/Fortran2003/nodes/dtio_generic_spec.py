class Dtio_Generic_Spec(Base):  # R1208
    """
    ::

        <dtio-generic-spec> = READ ( FORMATTED )
                              | READ ( UNFORMATTED )
                              | WRITE ( FORMATTED )
                              | WRITE ( UNFORMATTED )

    Attributes::

        items : (str, )

    """

    subclass_names = []

    @staticmethod
    def match(string):
        for rw in ["READ", "WRITE"]:
            if string[: len(rw)].upper() == rw:
                line = string[len(rw) :].lstrip()
                if not line:
                    return
                if line[0] != "(" or line[-1] != ")":
                    return
                line = line[1:-1].strip().upper()
                if line in ["FORMATTED", "UNFORMATTED"]:
                    return ("%s(%s)" % (rw, line),)

    def tostr(self):
        return "%s" % (self.items[0])
