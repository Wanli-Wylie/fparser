


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

from scalar_char_initialization_expr import Scalar_Char_Initialization_Expr

class Language_Binding_Spec(Base):  # R509
    """
    Fortran2003 Rule R509::

        <language-binding-spec> = BIND ( C [ ,
            NAME = <scalar-char-initialization-expr> ] )

    """

    subclass_names = []
    use_names = ["Scalar_Char_Initialization_Expr"]

    @staticmethod
    def match(string):
        start = string[:4].upper()
        if start != "BIND":
            return
        line = string[4:].lstrip()
        if not line or line[0] + line[-1] != "()":
            return
        line = line[1:-1].strip()
        if not line:
            return
        start = line[0].upper()
        if start != "C":
            return
        line = line[1:].lstrip()
        if not line:
            return (None,)
        if not line.startswith(","):
            return
        line = line[1:].lstrip()
        start = line[:4].upper()
        if start != "NAME":
            return
        line = line[4:].lstrip()
        if not line.startswith("="):
            return
        return (Scalar_Char_Initialization_Expr(line[1:].lstrip()),)

    def tostr(self):
        if self.items[0] is None:
            return "BIND(C)"
        return "BIND(C, NAME = %s)" % (self.items[0])
