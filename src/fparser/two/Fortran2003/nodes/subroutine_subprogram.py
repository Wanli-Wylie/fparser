from fparser.two.utils import (
    BlockBase,
)

from end_subroutine_stmt import End_Subroutine_Stmt
from execution_part import Execution_Part
from internal_subprogram_part import Internal_Subprogram_Part
from specification_part import Specification_Part
from subroutine_stmt import Subroutine_Stmt

class Subroutine_Subprogram(BlockBase):  # R1231
    """
    ::

        <subroutine-subprogram> = <subroutine-stmt>
                                     [ <specification-part> ]
                                     [ <execution-part> ]
                                     [ <internal-subprogram-part> ]
                                  <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = [
        "Subroutine_Stmt",
        "Specification_Part",
        "Execution_Part",
        "Internal_Subprogram_Part",
        "End_Subroutine_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Subroutine_Stmt,
            [Specification_Part, Execution_Part, Internal_Subprogram_Part],
            End_Subroutine_Stmt,
            reader,
        )
