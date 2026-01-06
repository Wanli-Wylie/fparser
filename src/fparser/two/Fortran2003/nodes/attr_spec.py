


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

class Attr_Spec(STRINGBase):  # R503
    """
    ::

        <attr-spec> = <access-spec>
                      | ALLOCATABLE
                      | ASYNCHRONOUS
                      | DIMENSION ( <array-spec> )
                      | EXTERNAL
                      | INTENT ( <intent-spec> )
                      | INTRINSIC
                      | <language-binding-spec>
                      | OPTIONAL
                      | PARAMETER
                      | POINTER
                      | PROTECTED
                      | SAVE
                      | TARGET
                      | VALUE
                      | VOLATILE

    """

    subclass_names = [
        "Access_Spec",
        "Language_Binding_Spec",
        "Dimension_Attr_Spec",
        "Intent_Attr_Spec",
    ]
    use_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_attr_spec, string)


class Attr_Spec_List(SequenceBase):
    subclass_names = ["Attr_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)
