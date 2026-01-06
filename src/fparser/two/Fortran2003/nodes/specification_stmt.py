


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

class Specification_Stmt(Base):  # R212
    """
    ::

        <specification-stmt> = <access-stmt>
                               | <allocatable-stmt>
                               | <asynchronous-stmt>
                               | <bind-stmt>
                               | <common-stmt>
                               | <data-stmt>
                               | <dimension-stmt>
                               | <equivalence-stmt>
                               | <external-stmt>
                               | <intent-stmt>
                               | <intrinsic-stmt>
                               | <namelist-stmt>
                               | <optional-stmt>
                               | <pointer-stmt>
                               | <protected-stmt>
                               | <save-stmt>
                               | <target-stmt>
                               | <volatile-stmt>
                               | <value-stmt>

    """

    subclass_names = [
        "Access_Stmt",
        "Allocatable_Stmt",
        "Asynchronous_Stmt",
        "Bind_Stmt",
        "Comment",
        "Common_Stmt",
        "Data_Stmt",
        "Dimension_Stmt",
        "Equivalence_Stmt",
        "External_Stmt",
        "Intent_Stmt",
        "Intrinsic_Stmt",
        "Namelist_Stmt",
        "Optional_Stmt",
        "Pointer_Stmt",
        "Cray_Pointer_Stmt",
        "Protected_Stmt",
        "Save_Stmt",
        "Target_Stmt",
        "Volatile_Stmt",
        "Value_Stmt",
    ]
