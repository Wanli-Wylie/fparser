


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

from lower_bound import Lower_Bound
from upper_bound import Upper_Bound

class Explicit_Shape_Spec(SeparatorBase):  # R511
    """
    ::

        <explicit-shape-spec> = [ <lower-bound> : ] <upper-bound>

    """

    subclass_names = []
    use_names = ["Lower_Bound", "Upper_Bound"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        if ":" not in line:
            return None, Upper_Bound(string)
        lower, upper = line.split(":", 1)
        lower = lower.rstrip()
        upper = upper.lstrip()
        if not upper:
            return
        if not lower:
            return
        return Lower_Bound(repmap(lower)), Upper_Bound(repmap(upper))

    def tostr(self):
        if self.items[0] is None:
            return str(self.items[1])
        return SeparatorBase.tostr(self)


class Explicit_Shape_Spec_List(SequenceBase):
    subclass_names = ["Explicit_Shape_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Explicit_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)
