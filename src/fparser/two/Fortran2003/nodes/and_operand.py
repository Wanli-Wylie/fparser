


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

from level_4_expr import Level_4_Expr

class And_Operand(UnaryOpBase):  # R714
    """
    ::

        <and-operand> = [ <not-op> ] <level-4-expr>
        <not-op> = .NOT.

    """

    subclass_names = ["Level_4_Expr"]
    use_names = []

    @staticmethod
    def match(string):
        return UnaryOpBase.match(pattern.not_op.named(), Level_4_Expr, string)
