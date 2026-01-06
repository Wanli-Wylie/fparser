


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

from generic_spec import Generic_Spec

class End_Interface_Stmt(EndStmtBase):  # R1204
    """
    ::

        <end-interface-stmt> = END INTERFACE [ <generic-spec> ]

    Attributes::

        items : (Generic_Spec, )

    """

    subclass_names = []
    use_names = ["Generic_Spec"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "INTERFACE", Generic_Spec, string, require_stmt_type=True
        )
