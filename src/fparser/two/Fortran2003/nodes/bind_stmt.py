


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

from bind_entity import Bind_Entity_List
from language_binding_spec import Language_Binding_Spec

class Bind_Stmt(StmtBase):  # R522
    """
    Fortran2003 Rule R522::

        <bind-stmt> = <language-binding-spec> [ :: ] <bind-entity-list>

    """

    subclass_names = []
    use_names = ["Language_Binding_Spec", "Bind_Entity_List"]

    @staticmethod
    def match(string):
        i = string.find("::")
        if i == -1:
            i = string.find(")")
            if i == -1:
                return
            lhs, rhs = string[:i], string[i + 1 :]
        else:
            lhs, rhs = string.split("::", 1)
        lhs = lhs.rstrip()
        rhs = rhs.lstrip()
        if not lhs or not rhs:
            return
        return Language_Binding_Spec(lhs), Bind_Entity_List(rhs)

    def tostr(self):
        return "%s :: %s" % self.items
