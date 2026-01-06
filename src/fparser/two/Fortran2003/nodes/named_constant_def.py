


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

from initialization_expr import Initialization_Expr
from named_constant import Named_Constant

class Named_Constant_Def(KeywordValueBase):  # R539
    """
    ::

        <named-constant-def> = <named-constant> = <initialization-expr>

    """

    subclass_names = []
    use_names = ["Named_Constant", "Initialization_Expr"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Named_Constant, Initialization_Expr, string)


class Named_Constant_Def_List(SequenceBase):
    subclass_names = ["Named_Constant_Def"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Named_Constant_Def, string)

    def __iter__(self):
        return iter(self.items)
