


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

from local_defined_operator import Local_Defined_Operator
from name import Local_Name
from name import Use_Name
from use_defined_operator import Use_Defined_Operator

class Rename(Base):  # R1111
    """
    Class defining Rule #R1111::

        rename is local-name => use-name
               or OPERATOR(local-defined-operator) => OPERATOR(use-defined-operator)

    where::

        local-defined-operator is defined-uary-op or defined-binary-op
        defined-binary-op is .letter [letter] ... .

    """

    subclass_names = []
    use_names = [
        "Local_Name",
        "Use_Name",
        "Local_Defined_Operator",
        "Use_Defined_Operator",
    ]

    @staticmethod
    def match(string):
        """
        :param str string: the string to attempt to match.

        :returns: three tuple containing description, local name, remote name.
        :rtype: Optional[ \
                    Tuple[Optional[str], \
                          :py:class:`fparser.two.Fortran2003.Local_Name` | \
                          :py:class:`fparser.two.Fortran2003.Local_Defined_Operator`, \
                          :py:class:`fparser.two.Fortran2003.Use_Name` | \
                          :py:class:`fparser.two.Fortran2003.Use_Defined_Operator`]]
        """
        parts = string.split("=>", 1)
        if len(parts) != 2:
            return None
        lhs, rhs = parts[0].rstrip(), parts[1].lstrip()
        if not lhs or not rhs:
            return None
        if lhs[:8].upper() == "OPERATOR" and rhs[:8].upper() == "OPERATOR":
            tmp = lhs[8:].lstrip()
            rhs_op = rhs[8:].lstrip()
            if tmp and rhs_op and tmp[0] == "(" and tmp[-1] == ")":
                if rhs_op[0] != "(" or rhs_op[-1] != ")":
                    return None
                tmp = tmp[1:-1].strip()
                rhs_op = rhs_op[1:-1].strip()
                if not tmp or not rhs_op:
                    return None
                return (
                    "OPERATOR",
                    Local_Defined_Operator(tmp),
                    Use_Defined_Operator(rhs_op),
                )
        return None, Local_Name(lhs), Use_Name(rhs)

    def tostr(self):
        """
        :returns: the string representation of this Rename object.
        :rtype: str
        """
        if not self.items[0]:
            # Not an operator.
            return f"{self.children[1]} => {self.children[2]}"
        # This represents the renaming of an Operator.
        return (
            f"{self.children[0]}({self.children[1]}) => "
            f"{self.children[0]}({self.children[2]})"
        )


class Rename_List(SequenceBase):
    subclass_names = ["Rename"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Rename, string)

    def __iter__(self):
        return iter(self.items)
