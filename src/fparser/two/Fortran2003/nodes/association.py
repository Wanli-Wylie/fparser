from name import Associate_Name
from selector import Selector

class Association(BinaryOpBase):  # R818
    """
    <association> = <associate-name> => <selector>
    """

    subclass_names = []
    use_names = ["Associate_Name", "Selector"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Associate_Name, "=>", Selector, string)


class Association_List(SequenceBase):
    subclass_names = ["Association"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Association, string)

    def __iter__(self):
        return iter(self.items)
