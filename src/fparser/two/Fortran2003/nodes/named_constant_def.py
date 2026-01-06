from initialization_expr import Initialization_Expr
from named_constant import Named_Constant

class Named_Constant_Def(KeywordValueBase):  # R539
    """
    ::

        <named-constant-def> = <named-constant> = <initialization-expr>

    """

    subclass_names = []
    use_names = ["Named_Constant", "Initialization_Expr"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Named_Constant, Initialization_Expr, string)


class Named_Constant_Def_List(SequenceBase):
    subclass_names = ["Named_Constant_Def"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Named_Constant_Def, string)

    def __iter__(self):
        return iter(self.items)
