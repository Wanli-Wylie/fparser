


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

from io_implied_do_control import Io_Implied_Do_Control
from io_implied_do_object import Io_Implied_Do_Object_List

class Io_Implied_Do(Base):  # R917
    """
    ::

        <io-implied-do> = ( <io-implied-do-object-list> , <io-implied-do-control> )
    """

    subclass_names = []
    use_names = ["Io_Implied_Do_Object_List", "Io_Implied_Do_Control"]

    @staticmethod
    def match(string):
        if len(string) <= 9 or string[0] != "(" or string[-1] != ")":
            return
        line, repmap = string_replace_map(string[1:-1].strip())
        i = line.rfind("=")
        if i == -1:
            return
        j = line[:i].rfind(",")
        if j == -1:
            return
        return (
            Io_Implied_Do_Object_List(repmap(line[:j].rstrip())),
            Io_Implied_Do_Control(repmap(line[j + 1 :].lstrip())),
        )

    def tostr(self):
        return "(%s, %s)" % (self.items)
