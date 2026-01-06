


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

from int_expr import Scalar_Int_Expr
from label import Label_List

class Computed_Goto_Stmt(StmtBase):  # R846
    """
    <computed-goto-stmt> = GO TO ( <label-list> ) [ , ] <scalar-int-expr>
    """

    subclass_names = []
    use_names = ["Label_List", "Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        if string[:2].upper() != "GO":
            return
        line = string[2:].lstrip()
        if line[:2].upper() != "TO":
            return
        line = line[2:].lstrip()
        if not line.startswith("("):
            return
        i = line.find(")")
        if i == -1:
            return
        lst = line[1:i].strip()
        if not lst:
            return
        line = line[i + 1 :].lstrip()
        if line.startswith(","):
            line = line[1:].lstrip()
        if not line:
            return
        return Label_List(lst), Scalar_Int_Expr(line)

    def tostr(self):
        return "GO TO (%s), %s" % self.items
