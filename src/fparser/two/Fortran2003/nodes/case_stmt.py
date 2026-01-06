


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

from case_selector import Case_Selector
from name import Case_Construct_Name

class Case_Stmt(StmtBase):  # R810
    """
    <case-stmt> = CASE <case-selector> [ <case-construct-name> ]
    """

    subclass_names = []
    use_names = ["Case_Selector", "Case_Construct_Name"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "CASE":
            return
        line, repmap = string_replace_map(string[4:].lstrip())
        if line.startswith("("):
            i = line.find(")")
            if i == -1:
                return
            n = line[i + 1 :].lstrip() or None
            if n:
                n = Case_Construct_Name(repmap(n))
            return Case_Selector(repmap(line[: i + 1].rstrip())), n
        if line[:7].upper() == "DEFAULT":
            n = repmap(line[7:].lstrip()) or None
            if n:
                n = Case_Construct_Name(repmap(n))
            return Case_Selector(line[:7]), n

    def tostr(self):
        if self.items[1] is None:
            return "CASE %s" % (self.items[0])
        return "CASE %s %s" % (self.items)

    def get_end_name(self):
        """
        :return: the name at the END of this block, if it exists
        :rtype: str or NoneType
        """
        name = self.items[1]
        if name is not None:
            return name.string
        return None
