


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

from do_body import Do_Body
from do_term_shared_stmt import Do_Term_Shared_Stmt
from label_do_stmt import Label_Do_Stmt

class Inner_Shared_Do_Construct(BlockBase):  # R841
    """
    ::

        <inner-shared-do-construct> = <label-do-stmt>
                                          <do-body>
                                          <do-term-shared-stmt>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Do_Body", "Do_Term_Shared_Stmt"]

    @staticmethod
    def match(reader):
        content = []
        for cls in [Label_Do_Stmt, Do_Body, Do_Term_Shared_Stmt]:
            obj = cls(reader)
            if obj is None:  # todo: restore reader
                return
            content.append(obj)
        return (content,)
