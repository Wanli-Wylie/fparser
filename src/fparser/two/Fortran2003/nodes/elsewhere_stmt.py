


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

from name import Where_Construct_Name

class Elsewhere_Stmt(StmtBase, WORDClsBase):  # R750
    """
    <elsewhere-stmt> = ELSEWHERE [ <where-construct-name> ]
    """

    subclass_names = []
    use_names = ["Where_Construct_Name"]
    _regex = re.compile(r"ELSE\s*WHERE", re.I)

    @staticmethod
    def match(string):
        if not Elsewhere_Stmt._regex.match(string):
            return
        idx = string.upper().index("WHERE")
        line = string[idx + 5 :].lstrip()
        if line:
            return "ELSEWHERE", Where_Construct_Name(line)
        return "ELSEWHERE", None

    def get_end_name(self):
        """
        :return: the name at the END of this block, if it exists
        :rtype: str or NoneType
        """
        name = self.items[1]
        if name is not None:
            return name.string
        return None
