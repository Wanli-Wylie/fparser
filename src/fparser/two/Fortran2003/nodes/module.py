


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

from end_module_stmt import End_Module_Stmt
from module_stmt import Module_Stmt
from module_subprogram_part import Module_Subprogram_Part
from specification_part import Specification_Part

class Module(BlockBase):  # R1104
    """
    ::

        <module> = <module-stmt>
                       [ <specification-part> ]
                       [ <module-subprogram-part> ]
                       <end-module-stmt>

    """

    subclass_names = []
    use_names = [
        "Module_Stmt",
        "Specification_Part",
        "Module_Subprogram_Part",
        "End_Module_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Module_Stmt,
            [Specification_Part, Module_Subprogram_Part],
            End_Module_Stmt,
            reader,
        )
