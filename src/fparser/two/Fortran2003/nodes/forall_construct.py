


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

from end_forall_stmt import End_Forall_Stmt
from forall_body_construct import Forall_Body_Construct
from forall_construct_stmt import Forall_Construct_Stmt

class Forall_Construct(BlockBase):  # R752
    """
    ::

        <forall-construct> = <forall-construct-stmt>
                                 [ <forall-body-construct> ]...
                                 <end-forall-stmt>

    """

    subclass_names = []
    use_names = ["Forall_Construct_Stmt", "Forall_Body_Construct", "End_Forall_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Forall_Construct_Stmt,
            [Forall_Body_Construct],
            End_Forall_Stmt,
            reader,
            match_names=True,  # C732
            strict_match_names=True,  # C732
        )
