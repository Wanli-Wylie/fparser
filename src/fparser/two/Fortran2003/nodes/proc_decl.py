


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

from name import Procedure_Entity_Name
from null_init import Null_Init

class Proc_Decl(BinaryOpBase):  # R1214
    """
    ::

        <proc-decl> = <procedure-entity-name> [ => <null-init> ]

    Attributes::

        items : (Procedure_Entity_Name, Null_Init)

    """

    subclass_names = ["Procedure_Entity_Name"]
    use_names = ["Null_Init"]

    @staticmethod
    def match(string):
        return BinaryOpBase.match(Procedure_Entity_Name, "=>", Null_Init, string)


class Proc_Decl_List(SequenceBase):
    subclass_names = ["Proc_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Proc_Decl, string)

    def __iter__(self):
        return iter(self.items)
