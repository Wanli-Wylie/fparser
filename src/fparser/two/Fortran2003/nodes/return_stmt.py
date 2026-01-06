


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

class Return_Stmt(StmtBase):  # R1236
    """
    <return-stmt> = RETURN [ <scalar-int-expr> ]
    """

    subclass_names = []
    use_names = ["Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        start = string[:6].upper()
        if start != "RETURN":
            return
        if len(string) == 6:
            return (None,)
        return (Scalar_Int_Expr(string[6:].lstrip()),)

    def tostr(self):
        if self.items[0] is None:
            return "RETURN"
        return "RETURN %s" % self.items
