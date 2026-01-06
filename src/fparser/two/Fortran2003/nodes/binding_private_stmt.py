


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

class Binding_Private_Stmt(StmtBase, STRINGBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R449::

        <binding-private-stmt> = PRIVATE

    For binding private statement within the type-bound procedure
    part of a derived type.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match

        :return: keyword  "PRIVATE" or None if no match is found
        :rtype: str or None
        """
        return StringBase.match("PRIVATE", string.upper())
