class V(Base):  # R1010
    """
    ::

        v is signed-int-literal-constant

    Subject to the constraint::

        C1007: w is without kind parameters.

    """

    subclass_names = ["Signed_Int_Literal_Constant"]


class V_List(SequenceBase):
    subclass_names = ["V"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", V, string)

    def __iter__(self):
        return iter(self.items)
