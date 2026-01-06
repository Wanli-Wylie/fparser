


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

from entity_decl import Entity_Decl

class Target_Entity_Decl(Entity_Decl):
    """
    ::

        <target-entity-decl> = <object-name> [ ( <array-spec> ) ]

    """

    subclass_names = []
    use_names = ["Object_Name", "Array_Spec"]

    @staticmethod
    def match(string):
        return Entity_Decl.match(string, target=True)


class Target_Entity_Decl_List(SequenceBase):
    subclass_names = ["Target_Entity_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Target_Entity_Decl, string)

    def __iter__(self):
        return iter(self.items)
