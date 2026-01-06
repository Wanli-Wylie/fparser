


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

from pointer_object import Pointer_Object_List

class Nullify_Stmt(StmtBase, CALLBase):  # R633
    """
    ::

        <nullify-stmt> = NULLIFY ( <pointer-object-list> )

    """

    subclass_names = []
    use_names = ["Pointer_Object_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("NULLIFY", Pointer_Object_List, string, require_rhs=True)
