


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
from specification_part import Specification_Part
from subroutine_stmt import Subroutine_Stmt

class Subroutine_Body(BlockBase):
    """
    ::

        <subroutine-body> = <subroutine-stmt>
                            [ <specification-part> ]
                          <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = ["Subroutine_Stmt", "Specification_Part", "End_Subroutine_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Subroutine_Stmt, [Specification_Part], End_Subroutine_Stmt, reader
        )
