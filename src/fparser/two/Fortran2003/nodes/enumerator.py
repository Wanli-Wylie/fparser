


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

from int_initialization_expr import Scalar_Int_Initialization_Expr
from named_constant import Named_Constant

class Enumerator(BinaryOpBase):  # R463
    """
    ::

        <enumerator> = <named-constant> [ = <scalar-int-initialization-expr> ]

    """

    subclass_names = ["Named_Constant"]
    use_names = ["Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string):
        if "=" not in string:
            return
        lhs, rhs = string.split("=", 1)
        return (
            Named_Constant(lhs.rstrip()),
            "=",
            Scalar_Int_Initialization_Expr(rhs.lstrip()),
        )


class Enumerator_List(SequenceBase):
    subclass_names = ["Enumerator"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Enumerator, string)

    def __iter__(self):
        return iter(self.items)
