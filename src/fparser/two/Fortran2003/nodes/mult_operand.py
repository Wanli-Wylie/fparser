


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

from level_1_expr import Level_1_Expr

class Mult_Operand(BinaryOpBase):  # R704
    """
    ::

        <mult-operand> = <level-1-expr> [ <power-op> <mult-operand> ]
        <power-op> = **

    """

    subclass_names = ["Level_1_Expr"]
    use_names = ["Mult_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_1_Expr, pattern.power_op.named(), Mult_Operand, string, right=False
        )
