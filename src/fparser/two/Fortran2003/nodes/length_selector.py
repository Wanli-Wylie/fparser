


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

from char_length import Char_Length
from type_param_value import Type_Param_Value

class Length_Selector(Base):  # R425
    """
    ::

        <length -selector> = ( [ LEN = ] <type-param-value> )
                            | * <char-length> [ , ]
    """

    subclass_names = []
    use_names = ["Type_Param_Value", "Char_Length"]

    @staticmethod
    def match(string):
        if string[0] + string[-1] == "()":
            line = string[1:-1].strip()
            if line[:3].upper() == "LEN" and line[3:].lstrip().startswith("="):
                line = line[3:].lstrip()
                line = line[1:].lstrip()
            return "(", Type_Param_Value(line), ")"
        if not string.startswith("*"):
            return
        line = string[1:].lstrip()
        if string[-1] == ",":
            line = line[:-1].rstrip()
        return "*", Char_Length(line)

    def tostr(self):
        if len(self.items) == 2:
            return "%s%s" % tuple(self.items)
        return "%sLEN = %s%s" % tuple(self.items)
