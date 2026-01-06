


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

from ac_do_variable import Ac_Do_Variable
from int_expr import Scalar_Int_Expr

class Ac_Implied_Do_Control(Base):
    """
    Fortran2003 rule R471.
    Specifies the syntax for the control of an implicit loop within an
    array constructor::

        ac-implied-do-control is ac-do-variable = scalar-int-expr,
                                        scalar-int-expr [ , scalar-int-expr ]

    where (R472) ac-do-variable is scalar-int-variable

    """

    subclass_names = []
    use_names = ["Ac_Do_Variable", "Scalar_Int_Expr"]

    @staticmethod
    def match(string):
        """ Attempts to match the supplied string with the pattern for
        implied-do control.

        :param str string: the string to test for a match.

        :returns: None if there is no match or a 2-tuple containing the \
                  do-variable name and the list of integer expressions (for \
                  start, stop [, step]).
        :rtype: NoneType or \
                (:py:class:`fparser.two.Fortran2003.Ac_Do_Variable`, list)
        """
        idx = string.find("=")
        if idx == -1:
            return None
        do_var = string[:idx].rstrip()
        line, repmap = string_replace_map(string[idx + 1 :].lstrip())
        int_exprns = line.split(",")
        if not (2 <= len(int_exprns) <= 3):
            return None
        exprn_list = [Scalar_Int_Expr(repmap(s.strip())) for s in int_exprns]
        return Ac_Do_Variable(do_var), exprn_list

    def tostr(self):
        return "%s = %s" % (self.items[0], ", ".join(map(str, self.items[1])))
