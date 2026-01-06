


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

from implicit_part_stmt import Implicit_Part_Stmt

class Implicit_Part(BlockBase):  # R205
    """
    Fortran2003 Rule R205::

        <implicit-part> = [ <implicit-part-stmt> ]...
                            <implicit-stmt>
    """

    subclass_names = []
    use_names = ["Implicit_Part_Stmt", "Implicit_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(None, [Implicit_Part_Stmt], None, reader)
