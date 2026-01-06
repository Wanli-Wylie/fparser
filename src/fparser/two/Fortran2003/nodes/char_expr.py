


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

from binary_constant import Binary_Constant
from complex_literal_constant import Complex_Literal_Constant
from expr import Expr
from hex_constant import Hex_Constant
from int_literal_constant import Int_Literal_Constant
from logical_literal_constant import Logical_Literal_Constant
from octal_constant import Octal_Constant
from real_literal_constant import Real_Literal_Constant
from signed_int_literal_constant import Signed_Int_Literal_Constant
from signed_real_literal_constant import Signed_Real_Literal_Constant

class Char_Expr(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R725::

        char-expr is expr

    C706 char-expr shall be of type character.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """Implements the matching for a character expression.

        :param str string: Fortran code to check for a match.
        :returns: `None` if there is no match, or an fparser2 class \
                  instance containing the matched expression.
        :rtype: NoneType or :py:class:`fparser.two.utils.Base`

        """
        excluded = (
            Signed_Int_Literal_Constant,
            Int_Literal_Constant,
            Binary_Constant,
            Octal_Constant,
            Hex_Constant,
            Signed_Real_Literal_Constant,
            Real_Literal_Constant,
            Complex_Literal_Constant,
            Logical_Literal_Constant,
        )
        # Attempt to match as a general expression.
        result = Expr(string)
        # C706: the match should fail if the result is not a character
        # expression. This is difficult to check in general so for the
        # time being check that, in the case where a literal constant
        # is returned, this is not of the wrong type.
        if isinstance(result, excluded):
            return None
        return result


class Scalar_Char_Expr(Base):
    subclass_names = ["Char_Expr"]
