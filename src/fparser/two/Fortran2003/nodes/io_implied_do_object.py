


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

class Io_Implied_Do_Object(Base):  # R918
    """
    ::

        <io-implied-do-object> = <input-item>
                                 | <output-item>

    """

    subclass_names = ["Input_Item", "Output_Item"]


class Io_Implied_Do_Object_List(SequenceBase):
    subclass_names = ["Io_Implied_Do_Object"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Io_Implied_Do_Object, string)

    def __iter__(self):
        return iter(self.items)
