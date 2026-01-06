


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

from designator import Designator
from name import Type_Param_Name

class Type_Param_Inquiry(BinaryOpBase):  # R615
    """
    ::

        <type-param-inquiry> = <designator> % <type-param-name>

    """

    subclass_names = []
    use_names = ["Designator", "Type_Param_Name"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(
            Designator, pattern.percent_op.named(), Type_Param_Name, string
        )
