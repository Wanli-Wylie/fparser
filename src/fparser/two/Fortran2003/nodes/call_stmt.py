


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

from actual_arg_spec import Actual_Arg_Spec_List
from procedure_designator import Procedure_Designator

class Call_Stmt(StmtBase):  # R1218
    """
    ::

        <call-stmt> = CALL <procedure-designator>
                      [ ( [ <actual-arg-spec-list> ] ) ]

    Attributes::

        items : (Procedure_Designator, Actual_Arg_Spec_List)

    """

    subclass_names = []
    use_names = ["Procedure_Designator", "Actual_Arg_Spec_List"]

    @staticmethod
    def match(string):
        if string[:4].upper() != "CALL":
            return
        line, repmap = string_replace_map(string[4:].lstrip())
        if line.endswith(")"):
            i = line.rfind("(")
            if i == -1:
                return
            args = repmap(line[i + 1 : -1].strip())
            if args:
                return (
                    Procedure_Designator(repmap(line[:i].rstrip())),
                    Actual_Arg_Spec_List(args),
                )
            return Procedure_Designator(repmap(line[:i].rstrip())), None
        return Procedure_Designator(string[4:].lstrip()), None

    def tostr(self):
        if self.items[1] is None:
            return "CALL %s" % (self.items[0])
        return "CALL %s(%s)" % self.items
