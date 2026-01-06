


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

class Binding_Attr(STRINGBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R453::

        <binding-attr> = PASS [ ( <arg-name> ) ]
                         | NOPASS
                         | NON_OVERRIDABLE
                         | DEFERRED
                         | <access-spec>

    Specifies syntax of allowed binding attributes for a
    specific type-bound procedure binding.

    """

    subclass_names = ["Access_Spec", "Binding_PASS_Arg_Name"]

    @staticmethod
    def match(string):
        """
        :return: keywords for allowed binding attributes or
                 nothing if no match is found
        :rtype: str
        """
        return STRINGBase.match(
            ["PASS", "NOPASS", "NON_OVERRIDABLE", "DEFERRED"], string
        )


class Binding_Attr_List(SequenceBase):
    subclass_names = ["Binding_Attr"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Binding_Attr, string)

    def __iter__(self):
        return iter(self.items)
