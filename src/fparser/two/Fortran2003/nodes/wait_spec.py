


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

from file_unit_number import File_Unit_Number
from int_expr import Scalar_Int_Expr
from int_variable import Scalar_Int_Variable
from iomsg_variable import Iomsg_Variable
from label import Label

class Wait_Spec(KeywordValueBase):  # R922
    """
    ::

        <wait-spec> = [ UNIT = ] <file-unit-number>
                      | END = <label>
                      | EOR = <label>
                      | ERR = <label>
                      | ID = <scalar-int-expr>
                      | IOMSG = <iomsg-variable>
                      | IOSTAT = <scalar-int-variable>

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "Label",
        "Scalar_Int_Expr",
        "Iomsg_Variable",
        "Scalar_Int_Variable",
    ]

    @staticmethod
    def match(string):
        for k, v in [
            (["END", "EOR", "ERR"], Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("ID", Scalar_Int_Expr),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)


class Wait_Spec_List(SequenceBase):
    subclass_names = ["Wait_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Wait_Spec, string)

    def __iter__(self):
        return iter(self.items)
