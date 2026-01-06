


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

from level_3_expr import Level_3_Expr

class Stop_Code(StringBase):  # R850
    """
    ::

        <stop-code> = <scalar-char-constant>
                      | <digit> [ <digit> [ <digit> [ <digit> [ <digit> ] ] ] ]
        Extension:
                      | Level_3_Expr
    """

    subclass_names = ["Scalar_Char_Constant"]

    @staticmethod
    def match(string):
        result = StringBase.match(pattern.abs_label, string)
        if result or not "extended-stop-args" in EXTENSIONS():
            return result
        # This will allow statements like `stop -1` and `stop str1//str2`
        return Level_3_Expr(string)
