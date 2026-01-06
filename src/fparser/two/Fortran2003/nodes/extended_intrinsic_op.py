


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

class Extended_Intrinsic_Op(StringBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R312::

        extended-intrinsic-op is intrinsic-operator

    Note, extended-intrinsic-op is only ever used by R311 and is
    defined in pattern_tools.py so could be matched directly in the
    Defined_Operator class (by changing it to STRINGBase and moving
    the match in this class into the Defined_Operator class). This
    would mean that this class would not be required. However, the
    parse tree would then not have the concept of an
    Extended_Intrinsic_Op which might be useful for code manipulation
    tools.

    """

    @staticmethod
    def match(string):
        """Implements the matching for the extended-intrinsic-op
        rule. Matches the string with the regular expression
        extended_intrinsic_operator in the pattern_tools file.

        :param str string: the string to match with the pattern rule.
        :return: a tuple of size 1 containing a string with the \
        matched name if there is a match, or None if there is not.
        :rtype: (str) or None

        """
        return StringBase.match(pattern.extended_intrinsic_operator, string)
