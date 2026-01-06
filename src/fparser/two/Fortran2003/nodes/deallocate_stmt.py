


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

from allocate_object import Allocate_Object_List
from dealloc_opt import Dealloc_Opt_List

class Deallocate_Stmt(StmtBase):  # R635
    """
    ::

        <deallocate-stmt> = DEALLOCATE ( <allocate-object-list> [
            , <dealloc-opt-list> ] )

    """

    subclass_names = []
    use_names = ["Allocate_Object_List", "Dealloc_Opt_List"]

    @staticmethod
    def match(string):
        if string[:10].upper() != "DEALLOCATE":
            return
        line = string[10:].lstrip()
        if not line or line[0] != "(" or line[-1] != ")":
            return
        line, repmap = string_replace_map(line[1:-1].strip())
        i = line.find("=")
        opts = None
        if i != -1:
            j = line[:i].rfind(",")
            assert j != -1, repr((i, j, line))
            opts = Dealloc_Opt_List(repmap(line[j + 1 :].lstrip()))
            line = line[:j].rstrip()
        return Allocate_Object_List(repmap(line)), opts

    def tostr(self):
        if self.items[1] is not None:
            return "DEALLOCATE(%s, %s)" % (self.items)
        return "DEALLOCATE(%s)" % (self.items[0])
