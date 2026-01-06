


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

from association import Association_List

class Associate_Stmt(StmtBase, CALLBase):  # R817
    """
    ::

        <associate-stmt> = [ <associate-construct-name> : ]
            ASSOCIATE ( <association-list> )

    """

    subclass_names = []
    use_names = ["Associate_Construct_Name", "Association_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("ASSOCIATE", Association_List, string)

    def get_start_name(self):
        return self.item.name
