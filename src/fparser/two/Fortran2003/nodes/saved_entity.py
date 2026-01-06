


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

from name import Common_Block_Name

class Saved_Entity(BracketBase):  # R544
    """
    ::

        <saved-entity> = <object-name>
                         | <proc-pointer-name>
                         | / <common-block-name> /

    """

    subclass_names = ["Object_Name", "Proc_Pointer_Name"]
    use_names = ["Common_Block_Name"]

    @staticmethod
    def match(string):
        return BracketBase.match("//", Common_Block_Name, string)


class Saved_Entity_List(SequenceBase):
    subclass_names = ["Saved_Entity"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Saved_Entity, string)

    def __iter__(self):
        return iter(self.items)
