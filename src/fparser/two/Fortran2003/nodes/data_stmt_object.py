from fparser.two.utils import (
    Base,
    SequenceBase,
)

class Data_Stmt_Object(Base):  # R526
    """
    Fortran 2003 Rule R526::

        <data-stmt-object> = <variable>
                             | <data-implied-do>

    """

    subclass_names = ["Variable", "Data_Implied_Do"]


class Data_Stmt_Object_List(SequenceBase):
    subclass_names = ["Data_Stmt_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Data_Stmt_Object, string)

    def __iter__(self):
        return iter(self.items)
