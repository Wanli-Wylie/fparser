


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

from name import Do_Construct_Name

class End_Do_Stmt(EndStmtBase):  # pylint: disable=invalid-name
    """
    R834::

        <end-do-stmt> = END DO [ <do-construct-name> ]

    """

    subclass_names = []
    use_names = ["Do_Construct_Name"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: code line matching the "END DO" statement
        :rtype: string
        """
        return EndStmtBase.match(
            "DO", Do_Construct_Name, string, require_stmt_type=True
        )
