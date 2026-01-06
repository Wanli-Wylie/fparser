


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

from initialization_expr import Initialization_Expr
from null_init import Null_Init

class Initialization(Base):  # R506
    """
    ::

        <initialization> =  = <initialization-expr>
                           | => <null-init>

    """

    subclass_names = []
    use_names = ["Initialization_Expr", "Null_Init"]

    @staticmethod
    def match(string):
        if string.startswith("=>"):
            return "=>", Null_Init(string[2:].lstrip())
        if string.startswith("="):
            return "=", Initialization_Expr(string[1:].lstrip())
        return None

    def tostr(self):
        return "%s %s" % self.items
