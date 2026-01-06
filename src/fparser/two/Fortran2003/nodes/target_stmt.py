


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

from target_entity_decl import Target_Entity_Decl_List

class Target_Stmt(StmtBase):  # R546
    """
    ::

        <target-stmt> = TARGET [ :: ] <target-entity-decl-list>

    """

    subclass_names = []
    use_names = ["Target_Entity_Decl_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "TARGET":
            return
        line = string[6:].lstrip()
        if line.startswith("::"):
            line = line[2:].lstrip()
        return (Target_Entity_Decl_List(line),)

    def tostr(self):
        return "TARGET :: %s" % (self.items[0])
