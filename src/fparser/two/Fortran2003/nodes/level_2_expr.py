


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

from add_operand import Add_Operand

class Level_2_Expr(BinaryOpBase):  # R706
    """
    ::

        <level-2-expr> = [ [ <level-2-expr> ] <add-op> ] <add-operand>
        <level-2-expr> = [ <level-2-expr> <add-op> ] <add-operand>
                         | <level-2-unary-expr>
        <add-op>   = +
                     | -

    """

    subclass_names = ["Level_2_Unary_Expr"]
    use_names = ["Level_2_Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Level_2_Expr, pattern.add_op.named(), Add_Operand, string
        )
