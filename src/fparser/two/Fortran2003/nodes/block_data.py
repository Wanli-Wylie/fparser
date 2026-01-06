


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

from block_data_stmt import Block_Data_Stmt
from end_block_data_stmt import End_Block_Data_Stmt
from specification_part import Specification_Part

class Block_Data(BlockBase):  # R1116
    """
    ::
        <block-data> = <block-data-stmt>
                           [ <specification-part> ]
                           <end-block-data-stmt>
    """

    subclass_names = []
    use_names = ["Block_Data_Stmt", "Specification_Part", "End_Block_Data_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Block_Data_Stmt, [Specification_Part], End_Block_Data_Stmt, reader
        )
