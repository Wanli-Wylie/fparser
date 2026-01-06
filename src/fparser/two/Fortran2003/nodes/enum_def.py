


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
