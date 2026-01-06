


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

from access_spec import Access_Spec
from generic_spec import Generic_Spec
from name import Binding_Name_List

class Generic_Binding(StmtBase):
    # pylint: disable=invalid-name
    """
    Fortran2003 Rule R452::

        <generic-binding> = GENERIC [ , <access-spec> ] ::
            <generic-spec> => <binding-name-list>

    Specifies the syntax of generic binding for a type-bound
    procedure within a derived type.

    """
    subclass_names = []
    use_names = ["Access_Spec", "Generic_Spec", "Binding_Name_List"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: 3-tuple containing strings and instances of the
                 classes describing a generic type-bound procedure
                 (optional access specifier, mandatory generic
                 identifier and mandatory binding name list)
        :rtype: 3-tuple of objects (2 mandatory and 1 optional)
        """
        # Incorrect 'GENERIC' statement
        if string[:7].upper() != "GENERIC":
            return
        line = string[7:].lstrip()
        i = line.find("::")
        # No mandatory double colon
        if i == -1:
            return
        aspec = None
        # Return optional access specifier (PRIVATE or PUBLIC)
        if line.startswith(","):
            aspec = Access_Spec(line[1:i].strip())
        line = line[i + 2 :].lstrip()
        i = line.find("=>")
        if i == -1:
            return
        # Return mandatory Generic_Spec and Binding_Name_List
        return (
            aspec,
            Generic_Spec(line[:i].rstrip()),
            Binding_Name_List(line[i + 3 :].lstrip()),
        )

    def tostr(self):
        """
        :return: parsed representation of a "GENERIC" type-bound procedure
        :rtype: str
        """
        if self.items[0] is None:
            return "GENERIC :: %s => %s" % (self.items[1:])
        return "GENERIC, %s :: %s => %s" % (self.items)
