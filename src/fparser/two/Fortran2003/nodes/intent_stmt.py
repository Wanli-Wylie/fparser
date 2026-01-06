


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

from dummy_arg_name import Dummy_Arg_Name_List
from intent_spec import Intent_Spec

class Intent_Stmt(StmtBase):  # R536
    """
    ::

        <intent-stmt> = INTENT ( <intent-spec> ) [ :: ] <dummy-arg-name-list>

    """

    subclass_names = []
    use_names = ["Intent_Spec", "Dummy_Arg_Name_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "INTENT":
            return
        line = string[6:].lstrip()
        if not line or not line.startswith("("):
            return
        i = line.rfind(")")
        if i == -1:
            return
        spec = line[1:i].strip()
        if not spec:
            return
        line = line[i + 1 :].lstrip()
        if line.startswith("::"):
            line = line[2:].lstrip()
        if not line:
            return
        return Intent_Spec(spec), Dummy_Arg_Name_List(line)

    def tostr(self):
        return "INTENT(%s) :: %s" % self.items
