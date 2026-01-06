


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

from end_do_stmt import End_Do_Stmt
from execution_part_construct import Execution_Part_Construct
from nonlabel_do_stmt import Nonlabel_Do_Stmt

class Block_Nonlabel_Do_Construct(BlockBase):  # pylint: disable=invalid-name
    """
    R826_2::

       <block-nonlabel-do-construct> = <nonlabel-do-stmt>
                                        [ <execution-part-construct> ]...
                                        <end-do-stmt>

    """

    subclass_names = []
    use_names = ["Nonlabel_Do_Stmt", "Execution_Part_Construct", "End_Do_Stmt"]

    @classmethod
    def match(cls, reader):
        """
        :param reader: instance of `FortranReaderBase` class
        :type reader: :py:class:`FortranReaderBase`
        :return: code block matching the nonlabeled "DO" construct
        :rtype: string
        """
        return BlockBase.match(
            cls.nonlabel_do_stmt_cls(),
            [Execution_Part_Construct],
            End_Do_Stmt,
            reader,
            match_names=True,  # C821
            strict_match_names=True,  # C821
        )

    @staticmethod
    def nonlabel_do_stmt_cls():
        """
        :returns: Fortran2003 Nonlabel_Do_Stmt class.
        :rtype: :py:class:`fparser.two.Fortran2003.Nonlabel_Do_Stmt`

        """
        return Nonlabel_Do_Stmt
