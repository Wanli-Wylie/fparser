class Alt_Return_Spec(Base):  # R1222
    """
    ::

        <alt-return-spec> = * <label>

    """

    subclass_names = []
    use_names = ["Label"]

    @staticmethod
    def match(string):
        if not string.startswith("*"):
            return
        line = string[1:].lstrip()
        if not line:
            return
        return (Label(line),)

    def tostr(self):
        return "*%s" % (self.items[0])
