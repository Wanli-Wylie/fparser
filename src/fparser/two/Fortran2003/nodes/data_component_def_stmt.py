


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

from component_attr_spec import Component_Attr_Spec_List
from component_decl import Component_Decl_List
from declaration_type_spec import Declaration_Type_Spec

class Data_Component_Def_Stmt(Type_Declaration_StmtBase):  # R440
    """
    Fortran 2003 rule 440::

        <data-component-def-stmt> is <declaration-type-spec> [
                 [ , <component-attr-spec-list> ] :: ] <component-decl-list>

    Associated constraints are::

        C436 (R440)  No component-attr-spec shall appear more than once in a given
             component-def-stmt.
        C437 (R440)  A component declared with the CLASS keyword shall have the
             ALLOCATABLE or POINTER attribute.
        C438 (R440)  If the POINTER attribute is not specified for a component,
             the declaration-type-spec in the component-def-stmt shall be CLASS(*)
             or shall specify an intrinsic type or a previously defined derived
             type.
        C439 (R440)  If the POINTER attribute is specified for a component, the
             declaration-type-spec in the component-def-stmt shall be CLASS(*) or
             shall specify an intrinsic type or any accessible derived type
             including the type being defined.
        C440 (R440)  If the POINTER or ALLOCATABLE attribute is specified, each
             component-array-spec shall be a deferred-shape-spec-list.
        C441 (R440)  If neither the POINTER attribute nor the ALLOCATABLE
             attribute is specified, each component-array-spec shall be an
             explicit-shape-spec-list.
        C443 (R440)  A component shall not have both the ALLOCATABLE and the
             POINTER attribute.
        C446 (R440)  If component-initialization appears, a double-colon separator
             shall appear before the component-decl-list.
        C447 (R440)  If => appears in component-initialization, POINTER shall
             appear in the component-attr-spec-list. If = appears in
             component-initialization, POINTER or ALLOCATABLE shall not appear in
             the component-attr-spec-list.

    C436-C441, C443, C446-C447 are currently not checked - issue #258.

    """

    subclass_names = []
    use_names = [
        "Declaration_Type_Spec",
        "Component_Attr_Spec_List",
        "Component_Decl_List",
    ]

    @staticmethod
    def match(string):
        return Type_Declaration_StmtBase.match(
            Declaration_Type_Spec, Component_Attr_Spec_List, Component_Decl_List, string
        )
