


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

from level_2_expr import Level_2_Expr

class Level_3_Expr(BinaryOpBase):  # R710
    """
    ::

        <level-3-expr> = [ <level-3-expr> <concat-op> ] <level-2-expr>
        <concat-op>    = //

    """

    subclass_names = ["Level_2_Expr"]
    use_names = ["Level_3_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_3_Expr, pattern.concat_op.named(), Level_2_Expr, string
        )
