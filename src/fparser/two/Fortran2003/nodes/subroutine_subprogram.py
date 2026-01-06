


import inspect
import re
import sys

from pathlib import Path
from typing import Union

from fparser.common.splitline import string_replace_map
from fparser.two import pattern_tools as pattern
from fparser.common.readfortran import FortranReaderBase
from fparser.two.symbol_table import SYMBOL_TABLES
from fparser.two.utils import (
    Base,
    BlockBase,
    StringBase,
    WORDClsBase,
    NumberBase,
    STRINGBase,
    BracketBase,
    StmtBase,
    EndStmtBase,
    BinaryOpBase,
    Type_Declaration_StmtBase,
    CALLBase,
    CallBase,
    KeywordValueBase,
    ScopingRegionMixin,
    SeparatorBase,
    SequenceBase,
    UnaryOpBase,
    walk,
    DynamicImport,
)
from fparser.two.utils import (
    EXTENSIONS,
    NoMatchError,
    FortranSyntaxError,
    InternalSyntaxError,
    InternalError,
    show_result,
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
