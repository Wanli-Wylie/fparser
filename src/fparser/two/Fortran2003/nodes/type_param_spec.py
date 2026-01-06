


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

from keyword import Keyword
from type_param_value import Type_Param_Value

class Type_Param_Spec(KeywordValueBase):  # R456
    """
    ::

        <type-param-spec> = [ <keyword> = ] <type-param-value>

    """

    subclass_names = ["Type_Param_Value"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Type_Param_Value, string)


class Type_Param_Spec_List(SequenceBase):
    subclass_names = ["Type_Param_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Param_Spec, string)

    def __iter__(self):
        return iter(self.items)
