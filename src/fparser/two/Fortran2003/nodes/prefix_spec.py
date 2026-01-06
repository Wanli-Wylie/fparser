


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

class Prefix_Spec(STRINGBase):  # R1228
    """
    ::

        <prefix-spec> = <declaration-type-spec>
                        | ELEMENTAL
                        | IMPURE
                        | MODULE
                        | PURE
                        | RECURSIVE

    """

    subclass_names = ["Declaration_Type_Spec"]
    # issue #221. IMPURE and MODULE are Fortran2008.
    keywords = ["ELEMENTAL", "IMPURE", "MODULE", "PURE", "RECURSIVE"]

    @staticmethod
    def match(string):
        """
        Matches procedure prefixes.

        :param str string: Candidate string.
        :return: Discovered prefix.
        :rtype: str
        """
        return STRINGBase.match(Prefix_Spec.keywords, string)
