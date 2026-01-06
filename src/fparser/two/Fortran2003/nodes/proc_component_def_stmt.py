


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

from proc_component_attr_spec import Proc_Component_Attr_Spec
from proc_component_attr_spec import Proc_Component_Attr_Spec_List
from proc_decl import Proc_Decl_List
from proc_interface import Proc_Interface

class Proc_Component_Def_Stmt(StmtBase):  # R445
    """
    ::

        <proc-component-def-stmt> is PROCEDURE ( [ <proc-interface> ] )
            , <proc-component-attr-spec-list> :: <proc-decl-list>

    where::

        proc-component-attr-spec is POINTER
                                 or PASS [ (arg-name) ]
                                 or NOPASS
                                 or access-spec

    The standard specifies the following constraints::

        C448 The same proc-component-attr-spec shall not appear more than once
             in a given proc-component-def-stmt. Not checked by fparser - #232.

        C449 POINTER shall appear in each proc-component-attr-spec-list.

        C450 If the procedure pointer component has an implicit interface or
             has no arguments, NOPASS shall be specified. Not checked by
             fparser - #232.

        C451 If PASS (arg-name) appears, the interface shall have a dummy argument
             named arg-name. Not checked by fparser - #232.

        C452 PASS and NOPASS shall not both appear in the same
             proc-component-attr-spec-list. Not checked by fparser - #232.

    """

    subclass_names = []
    use_names = ["Proc_Interface", "Proc_Component_Attr_Spec_List", "Proc_Decl_List"]

    @staticmethod
    def match(string):
        """
        Attempts to match the supplied string with the pattern for a
        declaration of a procedure part of a component.

        :param str string: the string to test for a match.

        :returns: None (if no match) or a tuple consisting of the procedure \
                  interface, the list of attributes and a list of procedure \
                  names or None.
        :rtype: NoneType or \
           (:py:class:`fparser.two.Fortran2003.Proc_Interface`, \
            :py:class:`fparser.two.Fortran2003.Proc_Component_Attr_Spec_List`,\
            :py:class:`fparser.two.Fortran2003.Proc_Decl_List`)
        """
        if string[:9].upper() != "PROCEDURE":
            return None
        line, repmap = string_replace_map(string[9:].lstrip())
        if not line.startswith("("):
            return None
        idx = line.find(")")
        if idx == -1:
            return None
        pinterface = repmap(line[: idx + 1])[1:-1].strip() or None
        if pinterface:
            pinterface = Proc_Interface(pinterface)
        line = line[idx + 1 :].lstrip()
        if not line.startswith(","):
            return None
        line = line[1:].strip()
        idx = line.find("::")
        if idx == -1:
            return None
        attr_spec_list = Proc_Component_Attr_Spec_List(repmap(line[:idx].rstrip()))
        # C449 POINTER must be present in the attribute list
        if Proc_Component_Attr_Spec("POINTER") not in attr_spec_list.items:
            return None
        return (
            pinterface,
            attr_spec_list,
            Proc_Decl_List(repmap(line[idx + 2 :].lstrip())),
        )

    def tostr(self):
        if self.items[0] is not None:
            return "PROCEDURE(%s), %s :: %s" % (self.items)
        return "PROCEDURE(), %s :: %s" % (self.items[1:])
