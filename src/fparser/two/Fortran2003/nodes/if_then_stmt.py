


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

from logical_expr import Scalar_Logical_Expr

class If_Then_Stmt(StmtBase):  # R803
    """
    ::

        <if-then-stmt> = [ <if-construct-name> : ]
            IF ( <scalar-logical-expr> ) THEN

    """

    subclass_names = []
    use_names = ["If_Construct_Name", "Scalar_Logical_Expr"]

    @staticmethod
    def match(string):
        if string[:2].upper() != "IF":
            return
        if string[-4:].upper() != "THEN":
            return
        line = string[2:-4].strip()
        if not line:
            return
        if line[0] + line[-1] != "()":
            return
        return (Scalar_Logical_Expr(line[1:-1].strip()),)

    def tostr(self):
        return "IF (%s) THEN" % self.items

    def get_start_name(self):
        return self.item.name
