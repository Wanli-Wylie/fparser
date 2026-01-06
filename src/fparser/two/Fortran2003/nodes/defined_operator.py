


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

class Defined_Operator(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R311::

        defined-operator is defined-unary-op
                          or defined-binary-op
                          or extended-intrinsic-op

    Note, defined-operator is defined in pattern_tools.py so could be
    called directly via a stringbase match. However, the defined unary
    and binary op rules have constraints which would not be checked if
    we did this.

    Note, whilst we subclass for both Defined Unary and Binary ops,
    the match is the same so we will only ever match with the first
    (so the second is not really necessary here). This is OK from a
    parsing point of view as they both return a Defined_Op class, so
    are identical from the parsers point of view.

    """

    subclass_names = ["Defined_Unary_Op", "Defined_Binary_Op", "Extended_Intrinsic_Op"]
