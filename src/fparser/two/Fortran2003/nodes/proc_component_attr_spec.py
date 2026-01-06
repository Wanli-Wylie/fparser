


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

class Proc_Component_Attr_Spec(STRINGBase):  # R446
    """
    ::

        <proc-component-attr-spec> = POINTER
                                     | PASS [ ( <arg-name> ) ]
                                     | NOPASS
                                     | <access-spec>

    """

    subclass_names = ["Access_Spec", "Proc_Component_PASS_Arg_Name"]

    @staticmethod
    def match(string):
        return STRINGBase.match(["POINTER", "PASS", "NOPASS"], string.upper())


class Proc_Component_Attr_Spec_List(SequenceBase):
    subclass_names = ["Proc_Component_Attr_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Proc_Component_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)
