


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

from loop_control import Loop_Control

class Nonlabel_Do_Stmt(StmtBase, WORDClsBase):  # pylint: disable=invalid-name
    """
    R829::

        <nonlabel-do-stmt> = [ <do-construct-name> : ] DO [ <loop-control> ]

    """

    subclass_names = []
    use_names = ["Do_Construct_Name", "Loop_Control"]

    @classmethod
    def match(cls, string):
        """
        :param str string: Fortran code to check for a match.
        :return: code line matching the nonlabeled "DO" statement.
        :rtype: str
        """
        return WORDClsBase.match("DO", cls.loop_control_cls(), string)

    @staticmethod
    def loop_control_cls():
        """
        :returns: Fortran2003 Loop_Control class.
        :rtype: :py:class:`fparser.two.Fortran2003.Loop_Control`

        """
        return Loop_Control

    def get_start_name(self):
        """
        :return: optional labeled "DO" statement name
        :rtype: str
        """
        return self.item.name
