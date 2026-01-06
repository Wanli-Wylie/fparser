


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

from lower_bound_expr import Lower_Bound_Expr

class Bounds_Spec(SeparatorBase):  # R737
    """
    ::

        <bounds-spec> = <lower-bound-expr> :

    """

    subclass_names = []
    use_names = ["Lower_Bound_Expr"]

    @staticmethod
    def match(string):
        return SeparatorBase.match(Lower_Bound_Expr, None, string, require_lhs=True)


class Bounds_Spec_List(SequenceBase):
    subclass_names = ["Bounds_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Bounds_Spec, string)

    def __iter__(self):
        return iter(self.items)
