


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

from declaration_type_spec import Declaration_Type_Spec
from letter_spec import Letter_Spec_List

class Implicit_Spec(CallBase):  # R550
    """
    ::

        <implicit-spec> = <declaration-type-spec> ( <letter-spec-list> )

    """

    subclass_names = []
    use_names = ["Declaration_Type_Spec", "Letter_Spec_List"]

    @staticmethod
    def match(string):
        if not string.endswith(")"):
            return
        i = string.rfind("(")
        if i == -1:
            return
        s1 = string[:i].rstrip()
        s2 = string[i + 1 : -1].strip()
        if not s1 or not s2:
            return
        return Declaration_Type_Spec(s1), Letter_Spec_List(s2)


class Implicit_Spec_List(SequenceBase):
    subclass_names = ["Implicit_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Implicit_Spec, string)

    def __iter__(self):
        return iter(self.items)
