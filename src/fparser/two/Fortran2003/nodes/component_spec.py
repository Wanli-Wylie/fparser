


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

from component_data_source import Component_Data_Source
from keyword import Keyword

class Component_Spec(KeywordValueBase):  # R458
    """
    ::

        <component-spec> = [ <keyword> = ] <component-data-source>

    """

    subclass_names = ["Component_Data_Source"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Component_Data_Source, string)


class Component_Spec_List(SequenceBase):
    subclass_names = ["Component_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Component_Spec, string)

    def __iter__(self):
        return iter(self.items)
