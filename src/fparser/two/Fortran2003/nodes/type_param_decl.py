


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
from name import Type_Param_Name

class Type_Param_Decl(BinaryOpBase):  # R436
    """
    ::
        <type-param-decl> = <type-param-name>
            [ = <scalar-int-initialization-expr> ]

    """

    subclass_names = ["Type_Param_Name"]
    use_names = ["Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string):
        if "=" not in string:
            return
        lhs, rhs = string.split("=", 1)
        lhs = lhs.rstrip()
        rhs = rhs.lstrip()
        if not lhs or not rhs:
            return
        return Type_Param_Name(lhs), "=", Scalar_Int_Initialization_Expr(rhs)


class Type_Param_Decl_List(SequenceBase):
    subclass_names = ["Type_Param_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Param_Decl, string)

    def __iter__(self):
        return iter(self.items)
