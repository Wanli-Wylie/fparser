


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

from access_id import Access_Id_List

class Access_Stmt(StmtBase, WORDClsBase):  # R518
    """
    Fortran2003 Rule R518::

        <access-stmt> = <access-spec> [ [ :: ] <access-id-list> ]

    """

    subclass_names = []
    use_names = ["Access_Spec", "Access_Id_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            ["PUBLIC", "PRIVATE"],
            Access_Id_List,
            string,
            colons=True,
            require_cls=False,
        )

    tostr = WORDClsBase.tostr_a
