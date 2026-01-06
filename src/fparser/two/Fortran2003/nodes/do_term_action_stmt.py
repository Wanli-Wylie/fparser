


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

class Do_Term_Action_Stmt(StmtBase):  # R838
    """
    ::

        <do-term-action-stmt> = <action-stmt>

    Notes::

        C824 - <do-term-action-stmt> shall not be <continue-stmt>, <goto-stmt>,
              <return-stmt>, <stop-stmt>, <exit-stmt>, <cycle-stmt>,
              <end-function-stmt>, <end-subroutine-stmt>, <end-program-stmt>,
              <arithmetic-if-stmt>

    """

    subclass_names = ["Action_Stmt_C824"]
