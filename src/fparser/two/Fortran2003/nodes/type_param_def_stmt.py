


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

from kind_selector import Kind_Selector
from type_param_attr_spec import Type_Param_Attr_Spec
from type_param_decl import Type_Param_Decl_List

class Type_Param_Def_Stmt(StmtBase):  # R435
    """
    ::

        <type-param-def-stmt> = INTEGER [ <kind-selector> ] ,
            <type-param-attr-spec> :: <type-param-decl-list>

    """

    subclass_names = []
    use_names = ["Kind_Selector", "Type_Param_Attr_Spec", "Type_Param_Decl_List"]

    @staticmethod
    def match(string):
        if string[:7].upper() != "INTEGER":
            return
        line, repmap = string_replace_map(string[7:].lstrip())
        if not line:
            return
        i = line.find(",")
        if i == -1:
            return
        kind_selector = repmap(line[:i].rstrip()) or None
        line = repmap(line[i + 1 :].lstrip())
        i = line.find("::")
        if i == -1:
            return
        l1 = line[:i].rstrip()
        l2 = line[i + 2 :].lstrip()
        if not l1 or not l2:
            return
        if kind_selector:
            kind_selector = Kind_Selector(kind_selector)
        return kind_selector, Type_Param_Attr_Spec(l1), Type_Param_Decl_List(l2)

    def tostr(self):
        s = "INTEGER"
        if self.items[0] is not None:
            s += "%s, %s :: %s" % tuple(self.items)
        else:
            s += ", %s :: %s" % tuple(self.items[1:])
        return s
