


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

from and_operand import And_Operand

class Or_Operand(BinaryOpBase):  # R715
    """
    ::

        <or-operand> = [ <or-operand> <and-op> ] <and-operand>
        <and-op> = .AND.

    """

    subclass_names = ["And_Operand"]
    use_names = ["Or_Operand", "And_Operand"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Or_Operand, pattern.and_op.named(), And_Operand, string
        )
