


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

from imag_part import Imag_Part
from real_part import Real_Part

class Complex_Literal_Constant(Base):  # R421
    """
    ::

        <complex-literal-constant> = ( <real-part>, <imag-part> )
    """

    subclass_names = []
    use_names = ["Real_Part", "Imag_Part"]

    @staticmethod
    def match(string):
        if not string or string[0] + string[-1] != "()":
            return
        if not pattern.abs_complex_literal_constant.match(string):
            return
        r, i = string[1:-1].split(",")
        return Real_Part(r.strip()), Imag_Part(i.strip())

    def tostr(self):
        return "(%s, %s)" % tuple(self.items)
