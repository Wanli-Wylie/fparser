


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

from name import Final_Subroutine_Name_List

class Final_Binding(StmtBase, WORDClsBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R454::

        <final-binding> = FINAL [ :: ] <final-subroutine-name-list>

    Specifies the syntax of final binding for a type-bound
    procedure within a derived type.

    """

    subclass_names = []
    use_names = ["Final_Subroutine_Name_List"]

    @staticmethod
    def match(string):
        """
        :return: keyword  "FINAL" with the list of "FINAL" type-bound
                 procedures or nothing if no match is found
        :rtype: str
        """
        return WORDClsBase.match(
            "FINAL", Final_Subroutine_Name_List, string, colons=True, require_cls=True
        )

    # String representation with optional double colons included
    tostr = WORDClsBase.tostr_a
