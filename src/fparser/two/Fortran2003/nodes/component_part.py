


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

from component_def_stmt import Component_Def_Stmt

class Component_Part(BlockBase):  # R438
    """
    ::

        <component-part> is [ <component-def-stmt> ]...

    """

    subclass_names = []
    use_names = ["Component_Def_Stmt"]

    @staticmethod
    def match(reader):
        content = []
        while 1:
            try:
                obj = Component_Def_Stmt(reader)
            except NoMatchError:
                obj = None
            if obj is None:
                break
            content.append(obj)
        if content:
            return (content,)
        return None

    def tofortran(self, tab="", isfix=None):
        """
        Converts this node (and all children) into Fortran.

        :param str tab: white space to prefix to output.
        :param bool isfix: whether or not to generate fixed-format output.

        :returns: Fortran code.
        :rtype: str

        """
        mylist = []
        for item in self.content:
            mylist.append(item.tofortran(tab=tab, isfix=isfix))
        return "\n".join(mylist)
