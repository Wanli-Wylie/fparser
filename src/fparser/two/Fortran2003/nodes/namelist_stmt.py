


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

from name import Namelist_Group_Name
from namelist_group_object import Namelist_Group_Object_List

class Namelist_Stmt(StmtBase):  # R552
    """
    Fortran 2003 rule R552::

        namelist-stmt is NAMELIST
                         / namelist-group-name / namelist-group-object-list
                         [ [,] / namelist-group-name /
                         namelist-group-object-list ] ...

    """

    subclass_names = []
    use_names = ["Namelist_Group_Name", "Namelist_Group_Object_List"]

    @staticmethod
    def match(string):
        """Implements the matching for a Namelist_Stmt.

        :param str string: a string containing the code to match.

        :returns: `None` if there is no match, otherwise a `tuple` \
            containing 2-tuples with a namelist name and a namelist object \
            list.
        :rtype: Optional[Tuple[Tuple[ \
            fparser.two.Fortran2003.Namelist_Group_Name, \
            fparser.two.Fortran2003.Namelist_Group_Object_List]]]

        """
        line = string.lstrip()
        if line[:8].upper() != "NAMELIST":
            return None
        line = line[8:].lstrip()
        if not line:
            return None
        parts = line.split("/")
        text_before_slash = parts.pop(0)
        if text_before_slash:
            return None
        items = []
        while len(parts) >= 2:
            name = parts.pop(0).strip()
            lst = parts.pop(0).strip()
            if lst.endswith(","):
                lst = lst[:-1].rstrip()
            items.append((Namelist_Group_Name(name), Namelist_Group_Object_List(lst)))
        if parts:
            # There is a missing second '/'
            return None
        return tuple(items)

    def tostr(self):
        """
        :returns: this Namelist_Stmt as a string.
        :rtype: str
        """
        return "NAMELIST " + ", ".join(f"/{name}/ {lst}" for name, lst in self.items)
