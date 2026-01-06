


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

from equiv_operand import Equiv_Operand

class Level_5_Expr(BinaryOpBase):  # R717
    """
    ::

        <level-5-expr> = [ <level-5-expr> <equiv-op> ] <equiv-operand>
        <equiv-op> = .EQV.
                   | .NEQV.

    """

    subclass_names = ["Equiv_Operand"]
    use_names = ["Level_5_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_5_Expr, pattern.equiv_op.named(), Equiv_Operand, string
        )
