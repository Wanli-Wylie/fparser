


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

from data_stmt_set import Data_Stmt_Set

class Data_Stmt(StmtBase):  # R524
    """
    Fortran 2003 Rule R524::

        <data-stmt> = DATA <data-stmt-set> [ [ , ] <data-stmt-set> ]...

    """

    subclass_names = []
    use_names = ["Data_Stmt_Set"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "DATA":
            return
        line, repmap = string_replace_map(string[4:].lstrip())
        i = line.find("/")
        if i == -1:
            return
        i = line.find("/", i + 1)
        if i == -1:
            return
        items = [Data_Stmt_Set(repmap(line[: i + 1]))]
        line = line[i + 1 :].lstrip()
        while line:
            if line.startswith(","):
                line = line[1:].lstrip()
            i = line.find("/")
            if i == -1:
                return
            i = line.find("/", i + 1)
            if i == -1:
                return
            items.append(Data_Stmt_Set(repmap(line[: i + 1])))
            line = line[i + 1 :].lstrip()
        return tuple(items)

    def tostr(self):
        return "DATA " + ", ".join(map(str, self.items))
