


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

from forall_header import Forall_Header

class Forall_Construct_Stmt(StmtBase, WORDClsBase):  # R753
    """
    ::

        <forall-construct-stmt> = [ <forall-construct-name> : ]
            FORALL <forall-header>

    """

    subclass_names = []
    use_names = ["Forall_Construct_Name", "Forall_Header"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("FORALL", Forall_Header, string, require_cls=True)

    def get_start_name(self):
        return self.item.name
