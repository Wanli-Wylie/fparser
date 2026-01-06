


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

from errmsg_variable import Errmsg_Variable
from stat_variable import Stat_Variable

class Dealloc_Opt(KeywordValueBase):  # R636
    """
    ::

        <dealloc-opt> = STAT = <stat-variable>
                        | ERRMSG = <errmsg-variable>

    """

    subclass_names = []
    use_names = ["Stat_Variable", "Errmsg_Variable"]

    @staticmethod
    def match(string):
        for k, v in [("STAT", Stat_Variable), ("ERRMSG", Errmsg_Variable)]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None


class Dealloc_Opt_List(SequenceBase):
    subclass_names = ["Dealloc_Opt"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Dealloc_Opt, string)

    def __iter__(self):
        return iter(self.items)
