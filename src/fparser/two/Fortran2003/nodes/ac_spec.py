


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

from ac_value import Ac_Value_List
from type_spec import Type_Spec

class Ac_Spec(Base):  # R466
    """
    ::

        <ac-spec> = <type-spec> ::
                    | [ <type-spec> :: ] <ac-value-list>

    """

    subclass_names = ["Ac_Value_List"]
    use_names = ["Type_Spec"]

    @staticmethod
    def match(string):
        if string.endswith("::"):
            return Type_Spec(string[:-2].rstrip()), None
        line, repmap = string_replace_map(string)
        i = line.find("::")
        if i == -1:
            return
        ts = line[:i].rstrip()
        line = line[i + 2 :].lstrip()
        ts = repmap(ts)
        line = repmap(line)
        return Type_Spec(ts), Ac_Value_List(line)

    def tostr(self):
        if self.items[0] is None:
            return str(self.items[1])
        if self.items[1] is None:
            return str(self.items[0]) + " ::"
        return "%s :: %s" % self.items
