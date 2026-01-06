


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

class Substring_Range(SeparatorBase):  # R611
    """
    ::

        <substring-range> = [ <scalar-int-expr> ] : [ <scalar-int-expr> ]

    """

    subclass_names = []
    use_names = ["Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Scalar_Int_Expr, Scalar_Int_Expr, string)
