


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

from label import Label

class Goto_Stmt(StmtBase):  # R845
    """
    <goto-stmt> = GO TO <label>
    """

    subclass_names = []
    use_names = ["Label"]

    @staticmethod
    def match(string):
        if string[:2].upper() != "GO":
            return
        line = string[2:].lstrip()
        if line[:2].upper() != "TO":
            return
        return (Label(line[2:].lstrip()),)

    def tostr(self):
        return "GO TO %s" % (self.items[0])
