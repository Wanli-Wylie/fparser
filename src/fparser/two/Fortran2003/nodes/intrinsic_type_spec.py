


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

from char_selector import Char_Selector
from kind_selector import Kind_Selector

class Intrinsic_Type_Spec(WORDClsBase):  # R403
    """
    ::

        <intrinsic-type-spec> = INTEGER [ <kind-selector> ]
                                | REAL [ <kind-selector> ]
                                | DOUBLE COMPLEX
                                | COMPLEX [ <kind-selector> ]
                                | CHARACTER [ <char-selector> ]
                                | LOGICAL [ <kind-selector> ]
        Extensions:
                                | DOUBLE PRECISION
                                | BYTE
    """

    subclass_names = []
    use_names = ["Kind_Selector", "Char_Selector"]

    @staticmethod
    def match(string):
        for w, cls in [
            ("INTEGER", Kind_Selector),
            ("REAL", Kind_Selector),
            ("COMPLEX", Kind_Selector),
            ("LOGICAL", Kind_Selector),
            ("CHARACTER", Char_Selector),
            (pattern.abs_double_complex_name, None),
            (pattern.abs_double_precision_name, None),
            ("BYTE", None),
        ]:
            try:
                obj = WORDClsBase.match(w, cls, string)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None
