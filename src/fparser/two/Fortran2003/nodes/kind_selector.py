


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

from char_length import Char_Length
from int_initialization_expr import Scalar_Int_Initialization_Expr

class Kind_Selector(Base):  # R404
    """
    Fortran 2003 rule R404::

        kind-selector is ( [ KIND = ] scalar-int-initialization-expr )

        A non-standard extension is also supported here:
                          | * char-length

    There is an associated constraint that we can't enforce in fparser::

        C404 (R404) The value of scalar-int-initialization-expr shall be
        nonnegative and shall specify a representation method that
        exists on the processor.

    """

    subclass_names = []
    use_names = ["Char_Length", "Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string):
        """Implements the matching for a Kind_Selector.

        :param str string: a string containing the code to match
        :return: `None` if there is no match, otherwise a `tuple` of \
        size 3 containing a '(', a single `list` which contains an \
        instance of classes that have matched and a ')', or a `tuple` \
        of size 2 containing a '*' and an instance of classes that \
        have matched.
        :rtype: `NoneType` or ( str, [ MatchedClasses ], str) or ( \
        str, :py:class:`fparser.two.Fortran2003.Char_Length`)

        :raises InternalError: if None is passed instead of a \
        string. The parent rule should not pass None and the logic in \
        this routine relies on a valid string.

        :raises InternalError: if the string passed is <=1 characters \
        long. The parent rule passing this string should ensure the \
        string is at least 2 characters long and the logic in this \
        routine relies on this. The reason there is a minimum of two \
        is that the pattern '*n' where 'n' is a number is the smallest \
        valid pattern. The other valid pattern must have at least a \
        name with one character surrounded by brackets e.g. '(x)' so \
        should be at least 3 characters long.

        """
        if string is None:
            raise InternalError(
                "String argument in class Kind_Selector method match() " "is None."
            )
        if len(string) <= 1:
            raise InternalError(
                "String argument '{0}' in class Kind_Selector method "
                "match() is too short to be valid.".format(string)
            )

        # remove any leading or trailing white space
        string = string.strip()

        if string[0] + string[-1] != "()":
            # must be the '*n' extension
            if not string.startswith("*"):
                return None
            return "*", Char_Length(string[1:].lstrip())
        # remove left and right brackets and subsequently any leading
        # or trailing spaces
        string = string[1:-1].strip()
        # check for optional 'kind='
        if len(string) > 5:
            # string is long enough to potentially contain 'kind=...'
            if string[:4].upper() == "KIND" and string[4:].lstrip()[0] == "=":
                # found 'kind=' so strip it out, including any leading spaces
                string = string[4:].lstrip()[1:].lstrip()
        return "(", Scalar_Int_Initialization_Expr(string), ")"

    def tostr(self):
        """
        :return: this kind_selector as a string
        :rtype: str
        """
        if len(self.items) == 2:
            result = "{0[0]}{0[1]}".format(self.items)
        elif len(self.items) == 3:
            result = "{0[0]}KIND = {0[1]}{0[2]}".format(self.items)
        else:
            raise InternalError(
                "Class Kind_Selector method tostr() has '{0}' items, "
                "but expecting 2 or 3.".format(len(self.items))
            )
        return result
