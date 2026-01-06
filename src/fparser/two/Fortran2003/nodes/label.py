class Label(StringBase):  # R313
    """
    ::

        <label> = <digit> [ <digit> [ <digit> [ <digit> [ <digit> ] ] ] ]

    Has attributes::

        string : str
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return StringBase.match(pattern.abs_label, string)

    def __int__(self):
        return int(self.string)


class Label_List(SequenceBase):
    subclass_names = ["Label"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Label, string)

    def __iter__(self):
        return iter(self.items)
