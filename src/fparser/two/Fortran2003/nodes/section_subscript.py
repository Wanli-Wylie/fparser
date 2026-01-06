from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Section_Subscript(Base):  # R619
    """
    ::

        <section-subscript> = <subscript>
                              | <subscript-triplet>
                              | <vector-subscript>

    """

    subclass_names = ["Subscript_Triplet", "Vector_Subscript", "Subscript"]


class Section_Subscript_List(SequenceBase):
    subclass_names = ["Section_Subscript"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Section_Subscript, string)

    def __iter__(self):
        return iter(self.items)
