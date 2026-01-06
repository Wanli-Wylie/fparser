


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

from proc_attr_spec import Proc_Attr_Spec_List
from proc_decl import Proc_Decl_List
from proc_interface import Proc_Interface

class Procedure_Declaration_Stmt(StmtBase):  # R1211
    """
    ::

        <procedure-declaration-stmt> = PROCEDURE ( [ <proc-interface> ] )
            [ [ , <proc-attr-spec> ]... :: ] <proc-decl-list>

    Attributes::

        items : (Proc_Interface, Proc_Attr_Spec_List, Proc_Decl_List)

    """

    subclass_names = []
    use_names = ["Proc_Interface", "Proc_Attr_Spec_List", "Proc_Decl_List"]

    @staticmethod
    def match(string):
        if string[:9].upper() != "PROCEDURE":
            return
        line = string[9:].lstrip()
        if not line.startswith("("):
            return
        line, repmap = string_replace_map(line)
        i = line.find(")")
        if i == -1:
            return
        tmp = line[1:i].strip()
        proc_interface = Proc_Interface(repmap(tmp)) if tmp else None
        line = line[i + 1 :].lstrip()
        i = line.find("::")
        proc_attr_spec_list = None
        if i != -1:
            tmp = line[:i].rstrip()
            if tmp and tmp[0] == ",":
                proc_attr_spec_list = Proc_Attr_Spec_List(repmap(tmp[1:].lstrip()))
            line = line[i + 2 :].lstrip()
        return proc_interface, proc_attr_spec_list, Proc_Decl_List(repmap(line))

    def tostr(self):
        r = "PROCEDURE"
        if self.items[0] is not None:
            r += "(%s)" % (self.items[0])
        else:
            r += "()"
        if self.items[1] is not None:
            r += ", %s ::" % (self.items[1])
        return "%s %s" % (r, self.items[2])
