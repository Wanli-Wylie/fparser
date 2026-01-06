


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

from or_operand import Or_Operand

class Equiv_Operand(BinaryOpBase):  # R716
    """
    ::

        <equiv-operand> = [ <equiv-operand> <or-op> ] <or-operand>
        <or-op>  = .OR.

    """

    subclass_names = ["Or_Operand"]
    use_names = ["Equiv_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Equiv_Operand, pattern.or_op.named(), Or_Operand, string
        )
