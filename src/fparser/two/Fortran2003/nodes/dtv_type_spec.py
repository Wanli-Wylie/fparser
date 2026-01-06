


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

from derived_type_spec import Derived_Type_Spec

class Dtv_Type_Spec(CALLBase):  # R920
    """
    ::

        <dtv-type-spec> = TYPE ( <derived-type-spec> )
                          | CLASS ( <derived-type-spec> )

    """

    subclass_names = []
    use_names = ["Derived_Type_Spec"]

    @staticmethod
    def match(string):
        return CALLBase.match(
            ["TYPE", "CLASS"], Derived_Type_Spec, string, require_rhs=True
        )
