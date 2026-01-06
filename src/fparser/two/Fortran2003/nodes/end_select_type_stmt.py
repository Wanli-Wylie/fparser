


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

from name import Select_Construct_Name

class End_Select_Type_Stmt(EndStmtBase):  # R824
    """
    <end-select-type-stmt> = END SELECT [ <select-construct-name> ]
    """

    subclass_names = []
    use_names = ["Select_Construct_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "SELECT", Select_Construct_Name, string, require_stmt_type=True
        )
