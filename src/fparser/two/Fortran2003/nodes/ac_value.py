


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

class Ac_Value(Base):  # R469
    """
    ::

        <ac-value> = <expr>
                     | <ac-implied-do>

    """

    subclass_names = ["Ac_Implied_Do", "Expr"]


class Ac_Value_List(SequenceBase):
    subclass_names = ["Ac_Value"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Ac_Value, string)

    def __iter__(self):
        return iter(self.items)
