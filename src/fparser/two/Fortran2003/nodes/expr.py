


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

from level_5_expr import Level_5_Expr

class Expr(BinaryOpBase):  # R722
    """
    ::

        <expr> = [ <expr> <defined-binary-op> ] <level-5-expr>
        <defined-binary-op> = . <letter> [ <letter> ]... .

    """

    subclass_names = ["Level_5_Expr"]
    use_names = ["Expr"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Expr,
            pattern.defined_binary_op.named(),
            Level_5_Expr,
            string,
            exclude_op_pattern=pattern.non_defined_binary_op,
        )


class Scalar_Expr(Base):
    subclass_names = ["Expr"]
