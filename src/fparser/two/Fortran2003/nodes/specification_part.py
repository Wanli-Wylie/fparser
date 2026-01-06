


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

from declaration_construct import Declaration_Construct
from implicit_part import Implicit_Part
from import_stmt import Import_Stmt
from use_stmt import Use_Stmt

class Specification_Part(BlockBase):  # R204
    """
    Fortran2003 Rule R204::

        <specification-part> = [ <use-stmt> ]...
                                 [ <import-stmt> ]...
                                 [ <implicit-part> ]
                                 [ <declaration-construct> ]...
    """

    subclass_names = []
    use_names = ["Use_Stmt", "Import_Stmt", "Implicit_Part", "Declaration_Construct"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            None,
            [Use_Stmt, Import_Stmt, Implicit_Part, Declaration_Construct],
            None,
            reader,
        )
