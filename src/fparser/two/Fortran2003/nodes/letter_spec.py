


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

class Letter_Spec(Base):  # R551
    """
    ::

        <letter-spec> = <letter> [ - <letter> ]

    """

    subclass_names = []

    @staticmethod
    def match(string):
        if len(string) == 1:
            lhs = string.upper()
            if "A" <= lhs <= "Z":
                return lhs, None
            return
        if "-" not in string:
            return
        lhs, rhs = string.split("-", 1)
        lhs = lhs.strip().upper()
        rhs = rhs.strip().upper()
        if not len(lhs) == len(rhs) == 1:
            return
        if not ("A" <= lhs <= rhs <= "Z"):
            return
        return lhs, rhs

    def tostr(self):
        if self.items[1] is None:
            return str(self.items[0])
        return "%s - %s" % tuple(self.items)


class Letter_Spec_List(SequenceBase):
    subclass_names = ["Letter_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Letter_Spec, string)

    def __iter__(self):
        return iter(self.items)
