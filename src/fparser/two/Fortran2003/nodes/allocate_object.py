from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Allocate_Object(Base):  # R629
    """
    ::

        <allocate-object> = <variable-name>
                            | <structure-component>

    """

    subclass_names = ["Variable_Name", "Structure_Component"]


class Allocate_Object_List(SequenceBase):
    subclass_names = ["Allocate_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Allocate_Object, string)

    def __iter__(self):
        return iter(self.items)
