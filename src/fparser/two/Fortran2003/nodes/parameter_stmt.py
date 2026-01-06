


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

from named_constant_def import Named_Constant_Def_List

class Parameter_Stmt(StmtBase, CALLBase):  # R538
    """
    ::

        <parameter-stmt> = PARAMETER ( <named-constant-def-list> )

    """

    subclass_names = []
    use_names = ["Named_Constant_Def_List"]

    @staticmethod
    def match(string):
        return CALLBase.match(
            "PARAMETER", Named_Constant_Def_List, string, require_rhs=True
        )
