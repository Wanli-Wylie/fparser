


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

from name import Associate_Name
from selector import Selector

class Association(BinaryOpBase):  # R818
    """
    <association> = <associate-name> => <selector>
    """

    subclass_names = []
    use_names = ["Associate_Name", "Selector"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Associate_Name, "=>", Selector, string)


class Association_List(SequenceBase):
    subclass_names = ["Association"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Association, string)

    def __iter__(self):
        return iter(self.items)
