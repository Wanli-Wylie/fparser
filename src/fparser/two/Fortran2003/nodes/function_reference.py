


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

from actual_arg_spec import Actual_Arg_Spec_List
from procedure_designator import Procedure_Designator

class Function_Reference(CallBase):  # R1217
    """
    <function-reference> = <procedure-designator>
        ( [ <actual-arg-spec-list> ] )
    """

    subclass_names = []
    use_names = ["Procedure_Designator", "Actual_Arg_Spec_List"]

    @staticmethod
    def match(string):
        return CallBase.match(Procedure_Designator, Actual_Arg_Spec_List, string)
