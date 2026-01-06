


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

from common_block_object import Common_Block_Object_List
from name import Common_Block_Name

class Common_Stmt(StmtBase):  # R557
    """
    ::

        <common-stmt> = COMMON [ / [ <common-block-name> ] / ]
            <common-block-object-list> [ [ , ] / [ <common-block-name> ]
            / <common-block-object-list> ]...
    """

    subclass_names = []
    use_names = ["Common_Block_Name", "Common_Block_Object_List"]

    @staticmethod
    def match(string):
        if string[:6].upper() != "COMMON":
            return
        line = string[6:]
        if not line or "A" <= line[0].upper() <= "Z" or line[0] == "_":
            return
        line, repmap = string_replace_map(line.lstrip())
        items = []
        if line.startswith("/"):
            i = line.find("/", 1)
            if i == -1:
                return
            name = line[1:i].strip() or None
            if name is not None:
                name = Common_Block_Name(name)
            line = line[i + 1 :].lstrip()
            i = line.find("/")
            if i == -1:
                lst = Common_Block_Object_List(repmap(line))
                line = ""
            else:
                tmp = line[:i].rstrip()
                if tmp.endswith(","):
                    tmp = tmp[:-1].rstrip()
                if not tmp:
                    return
                lst = Common_Block_Object_List(repmap(tmp))
                line = line[i:].lstrip()
        else:
            name = None
            i = line.find("/")
            if i == -1:
                lst = Common_Block_Object_List(repmap(line))
                line = ""
            else:
                tmp = line[:i].rstrip()
                if tmp.endswith(","):
                    tmp = tmp[:-1].rstrip()
                if not tmp:
                    return
                lst = Common_Block_Object_List(repmap(tmp))
                line = line[i:].lstrip()
        items.append((name, lst))
        while line:
            if line.startswith(","):
                line = line[1:].lstrip()
            if not line.startswith("/"):
                return
            i = line.find("/", 1)
            name = line[1:i].strip() or None
            if name is not None:
                name = Common_Block_Name(name)
            line = line[i + 1 :].lstrip()
            i = line.find("/")
            if i == -1:
                lst = Common_Block_Object_List(repmap(line))
                line = ""
            else:
                tmp = line[:i].rstrip()
                if tmp.endswith(","):
                    tmp = tmp[:-1].rstrip()
                if not tmp:
                    return
                lst = Common_Block_Object_List(repmap(tmp))
                line = line[i:].lstrip()
            items.append((name, lst))
        return (items,)

    def tostr(self):
        s = "COMMON"
        for name, lst in self.items[0]:
            if name is not None:
                s += " /%s/ %s" % (name, lst)
            else:
                s += " // %s" % (lst)
        return s
