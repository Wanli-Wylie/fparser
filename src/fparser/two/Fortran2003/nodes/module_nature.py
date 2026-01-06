


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

class Module_Nature(STRINGBase):  # pylint: disable=invalid-name
    """
    R1110::

        <module-nature> = INTRINSIC
                          | NON_INTRINSIC

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: keyword describing module nature ("INTRINSIC" or
                 "NON_INTRINSIC") or nothing if no match is found
        :rtype: string
        """
        return STRINGBase.match(["INTRINSIC", "NON_INTRINSIC"], string)
