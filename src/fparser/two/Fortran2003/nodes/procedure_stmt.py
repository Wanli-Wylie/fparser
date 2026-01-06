


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

from name import Procedure_Name_List

class Procedure_Stmt(StmtBase):  # R1206
    """
    ::

        <procedure-stmt> = [ MODULE ] PROCEDURE <procedure-name-list>

    Attributes::

        items : (Procedure_Name_List, )

    """

    subclass_names = []
    use_names = ["Procedure_Name_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() == "MODULE":
            line = string[6:].lstrip()
        else:
            line = string
        if line[:9].upper() != "PROCEDURE":
            return
        line = line[9:].lstrip()
        return (Procedure_Name_List(line),)

    def tostr(self):
        return "MODULE PROCEDURE %s" % (self.items[0])
