


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

from name import Type_Param_Name_List
from type_attr_spec import Type_Attr_Spec_List
from type_name import Type_Name

class Derived_Type_Stmt(StmtBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R430::

        derived-type-stmt is TYPE [ [ , type-attr-spec-list ] :: ]
                             type-name [ ( type-param-name-list ) ]

    """

    subclass_names = []
    use_names = ["Type_Attr_Spec_List", "Type_Name", "Type_Param_Name_List"]

    @staticmethod
    def match(string):
        """Implements the matching for a Derived Type Statement.

        :param str string: a string containing the code to match
        :return: `None` if there is no match, otherwise a `tuple` of \
                 size 3 containing an `Attribute_Spec_List` (or `None` if \
                 there isn't one), the name of the type (in a `Name` \
                 class) and a `Parameter_Name_List` (or `None` is there \
                 isn't one).
        :rtype: ( `Type_Attr_Spec_List` or `None`, `Name`, \
                  `Type_Param_Name_List` or `None` ) or `None`

        """
        string_strip = string.strip()
        if string_strip[:4].upper() != "TYPE":
            return None
        line = string_strip[4:].lstrip()
        position = line.find("::")
        attr_specs = None
        if position != -1:
            if line.startswith(","):
                lstrip = line[1:position].strip()
                if not lstrip:
                    # There is no content after the "," and before the
                    # "::"
                    return None
                attr_specs = Type_Attr_Spec_List(lstrip)
            elif line[:position].strip():
                # There is invalid content between and 'TYPE' and '::'
                return None
            line = line[position + 2 :].lstrip()
        match = pattern.name.match(line)
        if not match:
            # There is no content after the "TYPE" or the "::"
            return None
        name = Type_Name(match.group())
        line = line[match.end() :].lstrip()
        if not line:
            return attr_specs, name, None
        if line[0] + line[-1] != "()":
            return None
        return attr_specs, name, Type_Param_Name_List(line[1:-1].strip())

    def tostr(self):
        """
        :return: this derived type statement as a string
        :rtype: str
        :raises InternalError: if items array is not the expected size
        :raises InternalError: if items array[1] has no content

        """
        if len(self.items) != 3:
            raise InternalError(
                "Derived_Type_Stmt.tostr(). 'items' should be of size 3 but "
                "found '{0}'.".format(len(self.items))
            )
        if not self.items[1]:
            raise InternalError(
                "Derived_Type_Stmt.tostr(). 'items[1]' should be a Name "
                "instance containing the derived type name but it is empty"
            )
        string = "TYPE"
        if self.items[0]:
            string += ", {0} :: {1}".format(self.items[0], self.items[1])
        else:
            string += " :: {0}".format(self.items[1])
        if self.items[2]:
            string += "({0})".format(self.items[2])
        return string

    def get_start_name(self):
        """
        :return: this derived type statement's name as a string
        :rtype: str

        """
        return self.items[1].string
