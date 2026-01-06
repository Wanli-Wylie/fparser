


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

from stride import Stride
from subscript import Subscript

class Subscript_Triplet(Base):  # R620
    """
    ::

        <subscript-triplet> = [ <subscript> ] : [ <subscript> ] [ : <stride> ]

    """

    subclass_names = []
    use_names = ["Subscript", "Stride"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        t = line.split(":")
        if len(t) <= 1 or len(t) > 3:
            return
        lhs_obj, rhs_obj, stride_obj = None, None, None
        if len(t) == 2:
            lhs, rhs = t[0].rstrip(), t[1].lstrip()
        else:
            lhs, rhs, stride = t[0].rstrip(), t[1].strip(), t[2].lstrip()
            if stride:
                stride_obj = Stride(repmap(stride))
        if lhs:
            lhs_obj = Subscript(repmap(lhs))
        if rhs:
            rhs_obj = Subscript(repmap(rhs))
        return lhs_obj, rhs_obj, stride_obj

    def tostr(self):
        s = ""
        if self.items[0] is not None:
            s += str(self.items[0]) + " :"
        else:
            s += ":"
        if self.items[1] is not None:
            s += " " + str(self.items[1])
        if self.items[2] is not None:
            s += " : " + str(self.items[2])
        return s
