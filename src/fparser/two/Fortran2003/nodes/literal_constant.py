


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

class Literal_Constant(Base):  # R306
    """
    ::

        <literal-constant> = <int-literal-constant>
                             | <real-literal-constant>
                             | <complex-literal-constant>
                             | <logical-literal-constant>
                             | <char-literal-constant>
                             | <boz-literal-constant>
    """

    subclass_names = [
        "Int_Literal_Constant",
        "Real_Literal_Constant",
        "Complex_Literal_Constant",
        "Logical_Literal_Constant",
        "Char_Literal_Constant",
        "Boz_Literal_Constant",
    ]
