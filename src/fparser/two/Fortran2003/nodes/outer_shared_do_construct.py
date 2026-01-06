


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
from label_do_stmt import Label_Do_Stmt
from shared_term_do_construct import Shared_Term_Do_Construct

class Outer_Shared_Do_Construct(BlockBase):  # R839
    """
    ::

        <outer-shared-do-construct> = <label-do-stmt>
                                          <do-body>
                                          <shared-term-do-construct>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Do_Body", "Shared_Term_Do_Construct"]

    @staticmethod
    def match(reader):
        content = []
        for cls in [Label_Do_Stmt, Do_Body, Shared_Term_Do_Construct]:
            obj = cls(reader)
            if obj is None:  # todo: restore reader
                return
            content.append(obj)
        return (content,)
