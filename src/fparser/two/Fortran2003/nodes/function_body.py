


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

from end_function_stmt import End_Function_Stmt
from function_stmt import Function_Stmt
from specification_part import Specification_Part

class Function_Body(BlockBase):
    """
    ::

        <function-body> = <function-stmt>
                            [ <specification-part> ]
                          <end-function-stmt>

    """

    subclass_names = []
    use_names = ["Function_Stmt", "Specification_Part", "End_Function_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Function_Stmt, [Specification_Part], End_Function_Stmt, reader
        )
