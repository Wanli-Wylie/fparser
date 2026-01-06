


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

from object_name_deferred_shape_spec_list_item import Object_Name_Deferred_Shape_Spec_List_Item_List

class Allocatable_Stmt(StmtBase, WORDClsBase):  # R520
    """
    Fortran2003 Rule R520::

        <allocateble-stmt> = ALLOCATABLE [ :: ] <object-name> [
            ( <deferred-shape-spec-list> ) ] [ , <object-name>
            [ ( <deferred-shape-spec-list> ) ] ]...

    """

    subclass_names = []
    use_names = ["Object_Name_Deferred_Shape_Spec_List_Item_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "ALLOCATABLE",
            Object_Name_Deferred_Shape_Spec_List_Item_List,
            string,
            colons=True,
            require_cls=True,
        )
