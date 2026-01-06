


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

from end_interface_stmt import End_Interface_Stmt
from interface_specification import Interface_Specification
from interface_stmt import Interface_Stmt

class Interface_Block(BlockBase):  # R1201
    """
    ::

        <interface-block> = <interface-stmt>
                                [ <interface-specification> ]...
                                <end-interface-stmt>
    """

    subclass_names = []
    use_names = ["Interface_Stmt", "Interface_Specification", "End_Interface_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Interface_Stmt, [Interface_Specification], End_Interface_Stmt, reader
        )
