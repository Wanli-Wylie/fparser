


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

from saved_entity import Saved_Entity_List

class Save_Stmt(StmtBase, WORDClsBase):  # R543
    """
    ::

        <save-stmt> = SAVE [ [ :: ] <saved-entity-list> ]

    """

    subclass_names = []
    use_names = ["Saved_Entity_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "SAVE", Saved_Entity_List, string, colons=True, require_cls=False
        )

    tostr = WORDClsBase.tostr_a
