from fparser.two.utils import (
    BlockBase,
)

from component_part import Component_Part
from derived_type_stmt import Derived_Type_Stmt
from end_type_stmt import End_Type_Stmt
from private_or_sequence import Private_Or_Sequence
from type_bound_procedure_part import Type_Bound_Procedure_Part
from type_param_def_stmt import Type_Param_Def_Stmt

class Derived_Type_Def(BlockBase):  # R429
    """
    ::

        <derived-type-def> = <derived-type-stmt>
                               [ <type-param-def-stmt> ]...
                               [ <private-or-sequence> ]...
                               [ <component-part> ]
                               [ <type-bound-procedure-part> ]
                               <end-type-stmt>
    """

    subclass_names = []
    use_names = [
        "Derived_Type_Stmt",
        "Type_Param_Def_Stmt",
        "Private_Or_Sequence",
        "Component_Part",
        "Type_Bound_Procedure_Part",
        "End_Type_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Derived_Type_Stmt,
            [
                Type_Param_Def_Stmt,
                Private_Or_Sequence,
                Component_Part,
                Type_Bound_Procedure_Part,
            ],
            End_Type_Stmt,
            reader,
            match_names=True,  # C431
        )
