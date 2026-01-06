


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

from case_value_range import Case_Value_Range_List

class Case_Selector(Base):  # R813
    """
    ::

        <case-selector> = ( <case-value-range-list> )
                          | DEFAULT

    """

    subclass_names = []
    use_names = ["Case_Value_Range_List"]

    @staticmethod
    def match(string):
        if len(string) == 7 and string.upper() == "DEFAULT":
            return (None,)
        if not (string.startswith("(") and string.endswith(")")):
            return
        return (Case_Value_Range_List(string[1:-1].strip()),)

    def tostr(self):
        if self.items[0] is None:
            return "DEFAULT"
        return "(%s)" % (self.items[0])
