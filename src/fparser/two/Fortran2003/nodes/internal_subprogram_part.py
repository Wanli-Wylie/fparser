


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

from contains_stmt import Contains_Stmt
from internal_subprogram import Internal_Subprogram

class Internal_Subprogram_Part(BlockBase):  # R210
    """
    ::

        <internal-subprogram-part> = <contains-stmt>
                                       <internal-subprogram>
                                       [ <internal-subprogram> ]...

    """

    subclass_names = []
    use_names = ["Contains_Stmt", "Internal_Subprogram"]

    @staticmethod
    def match(reader):
        return BlockBase.match(Contains_Stmt, [Internal_Subprogram], None, reader)
