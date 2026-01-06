


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

from deferred_shape_spec import Deferred_Shape_Spec_List
from object_name import Object_Name

class Pointer_Decl(CallBase):  # R541
    """
    ::

        <pointer-decl> = <object-name> [ ( <deferred-shape-spec-list> ) ]
                         | <proc-entity-name>

    """

    subclass_names = ["Proc_Entity_Name", "Object_Name"]
    use_names = ["Deferred_Shape_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(
            Object_Name, Deferred_Shape_Spec_List, string, require_rhs=True
        )


class Pointer_Decl_List(SequenceBase):
    subclass_names = ["Pointer_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Pointer_Decl, string)

    def __iter__(self):
        return iter(self.items)
