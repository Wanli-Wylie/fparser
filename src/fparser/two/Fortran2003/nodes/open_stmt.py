


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

from connect_spec import Connect_Spec_List

class Open_Stmt(StmtBase, CALLBase):  # R904
    """
    R904 is:

    open-stmt is OPEN ( connect-spec-list )
    """

    subclass_names = []
    use_names = ["Connect_Spec_List"]

    @staticmethod
    def match(string):
        # The Connect_Spec_List class is generated automatically
        # by code at the end of this module
        return CALLBase.match("OPEN", Connect_Spec_List, string, require_rhs=True)
