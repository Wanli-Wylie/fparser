


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

from name import Arg_Name

class Binding_PASS_Arg_Name(CALLBase):
    # pylint: disable=invalid-name
    """
    Fortran 2003 helper rule (for R453)::

        <binding-PASS-arg-name> = PASS ( <arg-name> )

    Specifies the syntax of passed-object dummy argument for a
    specific type-bound procedure.

    """
    subclass_names = []
    use_names = ["Arg_Name"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: keyword  "PASS" with the name of a passed-object
                 dummy argument or nothing if no match is found
        :rtype: str
        """
        return CALLBase.match("PASS", Arg_Name, string)
