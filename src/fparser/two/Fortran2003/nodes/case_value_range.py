


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

from case_value import Case_Value

class Case_Value_Range(SeparatorBase):  # R814
    """
    ::

        <case-value-range> = <case-value>
                             | <case-value> :
                             | : <case-value>
                             | <case-value> : <case-value>

    """

    subclass_names = ["Case_Value"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Case_Value, Case_Value, string)


class Case_Value_Range_List(SequenceBase):
    subclass_names = ["Case_Value_Range"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Case_Value_Range, string)

    def __iter__(self):
        return iter(self.items)
