


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

class V(Base):  # R1010
    """
    ::

        v is signed-int-literal-constant

    Subject to the constraint::

        C1007: w is without kind parameters.

    """

    subclass_names = ["Signed_Int_Literal_Constant"]


class V_List(SequenceBase):
    subclass_names = ["V"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", V, string)

    def __iter__(self):
        return iter(self.items)
