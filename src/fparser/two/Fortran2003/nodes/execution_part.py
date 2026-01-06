


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

from executable_construct_c201 import Executable_Construct_C201
from execution_part_construct_c201 import Execution_Part_Construct_C201

class Execution_Part(BlockBase):  # R208
    """Fortran2003 Rule R208::

    <execution-part> = <executable-construct>
                       | [ <execution-part-construct> ]...

    <execution-part> shall not contain <end-function-stmt>,
    <end-program-stmt>, <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = ["Executable_Construct_C201", "Execution_Part_Construct_C201"]

    @staticmethod
    def match(string):
        return BlockBase.match(
            Executable_Construct_C201, [Execution_Part_Construct_C201], None, string
        )
