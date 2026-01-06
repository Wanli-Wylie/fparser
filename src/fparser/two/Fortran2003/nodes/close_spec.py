


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

from default_char_expr import Scalar_Default_Char_Expr
from file_unit_number import File_Unit_Number
from int_variable import Scalar_Int_Variable
from iomsg_variable import Iomsg_Variable
from label import Label

class Close_Spec(KeywordValueBase):  # R909
    """
    ::

        <close-spec> = [ UNIT = ] <file-unit-number>
                       | IOSTAT = <scalar-int-variable>
                       | IOMSG = <iomsg-variable>
                       | ERR = <label>
                       | STATUS = <scalar-default-char-expr>

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "Scalar_Default_Char_Expr",
        "Label",
        "Iomsg_Variable",
        "Scalar_Int_Variable",
    ]

    @staticmethod
    def match(string):
        for k, v in [
            ("ERR", Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("STATUS", Scalar_Default_Char_Expr),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)


class Close_Spec_List(SequenceBase):
    subclass_names = ["Close_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Close_Spec, string)

    def __iter__(self):
        return iter(self.items)
