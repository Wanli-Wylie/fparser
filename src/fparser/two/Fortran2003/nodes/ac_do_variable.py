


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

class Ac_Do_Variable(Base):
    """
    Fortran2003 rule R472.
    Specifies the permitted form of an implicit do-loop variable within an
    array constructor::

        ac-do-variable is scalar-int-variable
        ac-do-variable shall be a named variable

    Subject to the following constraint::

        C493 (R472) ac-do-variable shall be a named variable.

    C493 is currently not checked - issue #257.

    """

    subclass_names = ["Scalar_Int_Variable"]
