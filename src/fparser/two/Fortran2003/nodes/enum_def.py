from end_enum_stmt import End_Enum_Stmt
from enum_def_stmt import Enum_Def_Stmt
from enumerator_def_stmt import Enumerator_Def_Stmt

class Enum_Def(BlockBase):  # R460
    """
    ::

        <enum-def> = <enum-def-stmt>
                         <enumerator-def-stmt>
                         [ <enumerator-def-stmt> ]...
                         <end-enum-stmt>

    """

    subclass_names = []
    use_names = ["Enum_Def_Stmt", "Enumerator_Def_Stmt", "End_Enum_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Enum_Def_Stmt, [Enumerator_Def_Stmt], End_Enum_Stmt, reader
        )
