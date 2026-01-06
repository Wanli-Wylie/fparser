


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

from ac_spec import Ac_Spec

class Array_Constructor(BracketBase):  # R465
    """
    ::

        <array-constructor> = (/ <ac-spec> /)
                              | <left-square-bracket> <ac-spec>
                                <right-square-bracket>

    """

    subclass_names = []
    use_names = ["Ac_Spec"]

    @staticmethod
    def match(string):
        try:
            obj = BracketBase.match("(//)", Ac_Spec, string)
        except NoMatchError:
            obj = None
        if obj is None:
            obj = BracketBase.match("[]", Ac_Spec, string)
        return obj
