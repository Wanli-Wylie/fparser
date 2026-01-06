


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

class Label(StringBase):  # R313
    """
    ::

        <label> = <digit> [ <digit> [ <digit> [ <digit> [ <digit> ] ] ] ]

    Has attributes::

        string : str
    """

    subclass_names = []

    @staticmethod
    def match(string):
        return StringBase.match(pattern.abs_label, string)

    def __int__(self):
        return int(self.string)


class Label_List(SequenceBase):
    subclass_names = ["Label"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Label, string)

    def __iter__(self):
        return iter(self.items)
