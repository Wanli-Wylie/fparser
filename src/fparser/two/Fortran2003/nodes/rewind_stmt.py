


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

from file_unit_number import File_Unit_Number
from position_spec import Position_Spec_List

class Rewind_Stmt(StmtBase):  # R925
    """
    Fortran2003 Rule R925::

        <rewind-stmt> = REWIND <file-unit-number>
                        | REWIND ( <position-spec-list> )

    Attributes::

        items : (File_Unit_Number, Position_Spec_List)

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Position_Spec_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "REWIND":
            return
        line = string[6:].lstrip()
        if line.startswith("("):
            if not line.endswith(")"):
                return
            return None, Position_Spec_List(line[1:-1].strip())
        return File_Unit_Number(line), None

    def tostr(self):
        if self.items[0] is not None:
            assert self.items[1] is None, repr(self.items)
            return "REWIND %s" % (self.items[0])
        return "REWIND(%s)" % (self.items[1])
