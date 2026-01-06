


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

class Dtio_Generic_Spec(Base):  # R1208
    """
    ::

        <dtio-generic-spec> = READ ( FORMATTED )
                              | READ ( UNFORMATTED )
                              | WRITE ( FORMATTED )
                              | WRITE ( UNFORMATTED )

    Attributes::

        items : (str, )

    """

    subclass_names = []

    @staticmethod
    def match(string):
        for rw in ["READ", "WRITE"]:
            if string[: len(rw)].upper() == rw:
                line = string[len(rw) :].lstrip()
                if not line:
                    return
                if line[0] != "(" or line[-1] != ")":
                    return
                line = line[1:-1].strip().upper()
                if line in ["FORMATTED", "UNFORMATTED"]:
                    return ("%s(%s)" % (rw, line),)

    def tostr(self):
        return "%s" % (self.items[0])
