


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

from format import Format
from output_item import Output_Item_List

class Print_Stmt(StmtBase):  # R912
    """
    Fortran2003 Rule R912::

        <print-stmt> = PRINT <format> [ , <output-item-list> ]

    Parameters::

        items : (Format, Output_Item_List)

    """

    subclass_names = []
    use_names = ["Format", "Output_Item_List"]

    @staticmethod
    def match(string):
        if string[:5].upper() != "PRINT":
            return
        line = string[5:]
        if not line:
            return
        c = line[0].upper()
        if "A" <= c <= "Z" or c == "_" or "0" <= c <= "9":
            return
        line, repmap = string_replace_map(line.lstrip())
        i = line.find(",")
        if i == -1:
            return Format(repmap(line)), None
        tmp = repmap(line[i + 1 :].lstrip())
        if not tmp:
            return
        return Format(repmap(line[:i].rstrip())), Output_Item_List(tmp)

    def tostr(self):
        if self.items[1] is None:
            return "PRINT %s" % (self.items[0])
        return "PRINT %s, %s" % tuple(self.items)
