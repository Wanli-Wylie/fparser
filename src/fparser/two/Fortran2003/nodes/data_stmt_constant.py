


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

class Data_Stmt_Constant(Base):  # R532
    """
    Fortran 2003 Rule R532::

        <data-stmt-constant> = <scalar-constant>
                               | <scalar-constant-subobject>
                               | <signed-int-literal-constant>
                               | <signed-real-literal-constant>
                               | <null-init>
                               | <structure-constructor>

    """

    subclass_names = [
        "Scalar_Constant",
        "Scalar_Constant_Subobject",
        "Signed_Int_Literal_Constant",
        "Signed_Real_Literal_Constant",
        "Null_Init",
        "Structure_Constructor",
    ]
