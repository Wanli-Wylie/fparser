


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

from name import Associate_Name
from selector import Selector

class Select_Type_Stmt(StmtBase):  # R822
    """
    ::

        <select-type-stmt> = [ <select-construct-name> : ] SELECT TYPE
            ( [ <associate-name> => ] <selector> )

    """

    subclass_names = []
    use_names = ["Select_Construct_Name", "Associate_Name", "Selector"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "SELECT":
            return
        line = string[6:].lstrip()
        if line[:4].upper() != "TYPE":
            return
        line = line[4:].lstrip()
        if not line or line[0] + line[-1] != "()":
            return
        line = line[1:-1].strip()
        i = line.find("=>")
        if i != -1:
            return Associate_Name(line[:i].rstrip()), Selector(line[i + 2 :].lstrip())
        return None, Selector(line)

    def tostr(self):
        if self.items[0] is None:
            return "SELECT TYPE(%s)" % (self.items[1])
        return "SELECT TYPE(%s=>%s)" % (self.items)

    def get_start_name(self):
        return self.item.name
