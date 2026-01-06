


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

from pointer_decl import Pointer_Decl_List

class Pointer_Stmt(StmtBase, WORDClsBase):  # R540
    """
    ::

        <pointer-stmt> = POINTER [ :: ] <pointer-decl-list>

    """

    subclass_names = []
    use_names = ["Pointer_Decl_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "POINTER", Pointer_Decl_List, string, colons=True, require_cls=True
        )

    tostr = WORDClsBase.tostr_a
