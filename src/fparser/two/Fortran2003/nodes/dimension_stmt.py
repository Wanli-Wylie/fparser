


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

from array_spec import Array_Spec
from name import Array_Name

class Dimension_Stmt(StmtBase):  # R535
    """
    Fortran 2003 Rule R535::

        <dimension-stmt> = DIMENSION [ :: ] <array-name> ( <array-spec> )
            [ , <array-name> ( <array-spec> ) ]...

    """

    subclass_names = []
    use_names = ["Array_Name", "Array_Spec"]

    @staticmethod
    def match(string):
        if string[:9].upper() != "DIMENSION":
            return
        line, repmap = string_replace_map(string[9:].lstrip())
        if line.startswith("::"):
            line = line[2:].lstrip()
        decls = []
        for s in line.split(","):
            s = s.strip()
            if not s.endswith(")"):
                return
            i = s.find("(")
            if i == -1:
                return
            decls.append(
                (
                    Array_Name(repmap(s[:i].rstrip())),
                    Array_Spec(repmap(s[i + 1 : -1].strip())),
                )
            )
        if not decls:
            return
        return (decls,)

    def tostr(self):
        return "DIMENSION :: " + ", ".join(["%s(%s)" % ns for ns in self.items[0]])
