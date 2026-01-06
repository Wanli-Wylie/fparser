


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

class Executable_Construct(Base):  # R213
    # pylint: disable=invalid-name
    """
    Fortran 2003 rule R213::

        executable-construct is action-stmt
                             or associate-construct
                             or case-construct
                             or do-construct
                             or forall-construct
                             or if-construct
                             or select-type-construct
                             or where-construct

    """
    subclass_names = [
        "Action_Stmt",
        "Associate_Construct",
        "Case_Construct",
        "Do_Construct",
        "Forall_Construct",
        "If_Construct",
        "Select_Type_Construct",
        "Where_Construct",
    ]
