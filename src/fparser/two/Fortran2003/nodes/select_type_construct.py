


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

from end_select_type_stmt import End_Select_Type_Stmt
from execution_part_construct import Execution_Part_Construct
from select_type_stmt import Select_Type_Stmt
from type_guard_stmt import Type_Guard_Stmt

class Select_Type_Construct(BlockBase):  # R821
    """
    ::

        <select-type-construct> = <select-type-stmt>
                                      [ <type-guard-stmt>
                                        <block> == [<execution-part-construct>]..
                                      ]...
                                      <end-select-type-stmt>

    """

    subclass_names = []
    use_names = [
        "Select_Type_Stmt",
        "Type_Guard_Stmt",
        "Execution_Part_Construct",
        "End_Select_Type_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Select_Type_Stmt,
            [Type_Guard_Stmt, Execution_Part_Construct, Type_Guard_Stmt],
            End_Select_Type_Stmt,
            reader,
            match_names=True,  # C819
            strict_match_names=True,  # C819
            match_name_classes=(Type_Guard_Stmt),
        )
