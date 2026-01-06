


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

from actual_arg import Actual_Arg
from keyword import Keyword

class Actual_Arg_Spec(KeywordValueBase):  # R1220
    """
    <actual-arg-spec> = [ <keyword> = ] <actual-arg>
    """

    subclass_names = ["Actual_Arg"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Actual_Arg, string)


class Actual_Arg_Spec_List(SequenceBase):
    subclass_names = ["Actual_Arg_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Actual_Arg_Spec, string)

    def __iter__(self):
        return iter(self.items)
