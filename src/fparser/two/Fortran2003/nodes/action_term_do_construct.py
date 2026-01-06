


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

from do_term_action_stmt import Do_Term_Action_Stmt
from execution_part_construct import Execution_Part_Construct
from label_do_stmt import Label_Do_Stmt

class Action_Term_Do_Construct(BlockBase):  # R836
    """
    ::

        <action-term-do-construct> = <label-do-stmt>
                                         <do-body>
                                         <do-term-action-stmt>

        <action-term-do-construct> = <label-do-stmt>
                                     [ <execution-part-construct> ]...
                                     <do-term-action-stmt>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Execution_Part_Construct", "Do_Term_Action_Stmt"]

    @classmethod
    def match(cls, reader):
        return BlockBase.match(
            cls.label_do_stmt_cls(),
            [Execution_Part_Construct],
            Do_Term_Action_Stmt,
            reader,
            match_labels=True,
            enable_do_label_construct_hook=True,
        )

    @staticmethod
    def label_do_stmt_cls():
        """
        :returns: Fortran2003 Label_Do_Stmt class.
        :rtype: :py:class:`fparser.two.Fortran2003.Label_Do_Stmt`

        """
        return Label_Do_Stmt

    def tofortran(self, tab="", isfix=None):
        """
        Converts this node (and all children) into Fortran.

        :param str tab: white space to prefix to output.
        :param bool isfix: whether or not to generate fixed-format output.

        :returns: Fortran code.
        :rtype: str

        """
        line = []
        start = self.content[0]
        end = self.content[-1]
        extra_tab = "  "
        line.append(start.tofortran(tab=tab, isfix=isfix))
        for item in self.content[1:-1]:
            line.append(item.tofortran(tab=tab + extra_tab, isfix=isfix))
            if isinstance(item, self.label_do_stmt_cls()):
                extra_tab += "  "
        if len(self.content) > 1:
            line.append(end.tofortran(tab=tab, isfix=isfix))
        return "\n".join(line)
