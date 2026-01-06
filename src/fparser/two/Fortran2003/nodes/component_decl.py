


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
from component_array_spec import Component_Array_Spec
from component_initialization import Component_Initialization
from name import Component_Name

class Component_Decl(Base):  # R442
    """
    ::

        <component-decl> = <component-name> [ ( <component-array-spec> ) ]
            [ * <char-length> ] [ <component-initialization> ]

    """

    subclass_names = []
    use_names = [
        "Component_Name",
        "Component_Array_Spec",
        "Char_Length",
        "Component_Initialization",
    ]

    @staticmethod
    def match(string):
        m = pattern.name.match(string)
        if m is None:
            return
        name = Component_Name(m.group())
        newline = string[m.end() :].lstrip()
        if not newline:
            return name, None, None, None
        array_spec = None
        char_length = None
        init = None
        if newline.startswith("("):
            line, repmap = string_replace_map(newline)
            i = line.find(")")
            if i == -1:
                return
            array_spec = Component_Array_Spec(repmap(line[1:i].strip()))
            newline = repmap(line[i + 1 :].lstrip())
        if newline.startswith("*"):
            line, repmap = string_replace_map(newline)
            i = line.find("=")
            if i != -1:
                char_length = repmap(line[1:i].strip())
                newline = repmap(newline[i:].lstrip())
            else:
                char_length = repmap(newline[1:].strip())
                newline = ""
            char_length = Char_Length(char_length)
        if newline.startswith("="):
            init = Component_Initialization(newline)
        else:
            assert newline == "", repr(newline)
        return name, array_spec, char_length, init

    def tostr(self):
        s = str(self.items[0])
        if self.items[1] is not None:
            s += "(" + str(self.items[1]) + ")"
        if self.items[2] is not None:
            s += "*" + str(self.items[2])
        if self.items[3] is not None:
            s += " " + str(self.items[3])
        return s


class Component_Decl_List(SequenceBase):
    subclass_names = ["Component_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Component_Decl, string)

    def __iter__(self):
        return iter(self.items)
