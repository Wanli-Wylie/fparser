


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

from name import Import_Name_List

class Import_Stmt(StmtBase, WORDClsBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R1209::

        import-stmt is IMPORT [[ :: ] import-name-list ]

    C1210 (R1209) The IMPORT statement is allowed only in an
    interface-body. Note, this constraint is not currently enforced.

    C1211 (R1209) Each import-name shall be the name of an entity in
    the host scoping unit. This constraint is not currently enforced
    and can not be generally enforced as the name may come from a use
    statement without an only clause.

    """

    subclass_names = []
    use_names = ["Import_Name_List"]
    tostr = WORDClsBase.tostr_a

    @staticmethod
    def match(string):
        """
        Implements the matching for the import-stmt rule.

        Makes use of the WORDClsBase base class.

        :param str string: the string to match.

        :returns: None if there is no match, otherwise a tuple of size \
            2 containing the string `IMPORT` as the first entry and \
            an object of type `Import_Name_List` if names are \
            specified in the string or `None` if not.

        :rtype: None, or (str, \
            :py:class:`fparser.two.Fortran2003.Import_Name_List`) or \
            (str, None)

        """
        return WORDClsBase.match(
            "IMPORT", Import_Name_List, string, colons=True, require_cls=False
        )
