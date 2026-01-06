


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

from alloc_opt import Alloc_Opt_List
from allocation import Allocation_List
from type_spec import Type_Spec

class Allocate_Stmt(StmtBase):  # R623
    """
    Fortran2003 rule R623::

        allocate-stmt is ALLOCATE ( [ type-spec :: ] allocation-list
                                    [, alloc-opt-list ] )

    Subject to the following constraints:

    C622 (R629) Each allocate-object shall be a nonprocedure pointer or an
                 allocatable variable.
    C623 (R623) If any allocate-object in the statement has a deferred type
                parameter, either type-spec or SOURCE= shall appear.
    C624 (R623) If a type-spec appears, it shall specify a type with which
                each allocate-object is type compatible.
    C625 (R623) If any allocate-object is unlimited polymorphic, either
                type-spec or SOURCE= shall appear.
    C626 (R623) A type-param-value in a type-spec shall be an asterisk if and
                only if each allocate-object is a dummy argument for which the
                corresponding type parameter is assumed.
    C627 (R623) If a type-spec appears, the kind type parameter values of each
                allocate-object shall be the same as the corresponding type
                parameter values of the type-spec.
    C628 (R628) An allocate-shape-spec-list shall appear if and only if the
                allocate-object is an array.
    C629 (R628) The number of allocate-shape-specs in an
                allocate-shape-spec-list shall be the same as the rank of the
                allocate-object.
    C630 (R624) No alloc-opt shall appear more than once in a given
                alloc-opt-list.
    C631 (R623) If SOURCE= appears, type-spec shall not appear and
                allocation-list shall contain only one allocate-object, which
                shall be type compatible (5.1.1.2) with source-expr.
    C632 (R623) The source-expr shall be a scalar or have the same rank as
                allocate-object.
    C633 (R623) Corresponding kind type parameters of allocate-object and
                source-expr shall have the same values.

    None of these constraints are currently applied - issue #355.

    """

    subclass_names = []
    use_names = ["Type_Spec", "Allocation_List", "Alloc_Opt_List"]

    @classmethod
    def match(cls, string):
        """
        Attempts to match the supplied string as an Allocate_Stmt.

        :param str string: the string to attempt to match.

        :returns: A 2-tuple giving the Type_Spec and Allocation_List if the \
            match is successful, None otherwise.
        :rtype: Optional[ \
            Tuple[Optional[:py:class:`fparser.two.Fortran2003.Type_Spec`], \
                  :py:class:`fparser.two.Fortran2003.Allocation_List`]]
        """
        if string[:8].upper() != "ALLOCATE":
            return None
        line = string[8:].lstrip()
        if not line or line[0] != "(" or line[-1] != ")":
            return None
        line, repmap = string_replace_map(line[1:-1].strip())
        idx = line.find("::")
        spec = None
        if idx != -1:
            spec = Type_Spec(repmap(line[:idx].rstrip()))
            line = line[idx + 2 :].lstrip()
        idx = line.find("=")
        opts = None
        if idx != -1:
            jdx = line[:idx].rfind(",")
            if jdx == -1:
                # There must be at least one positional argument before any
                # named arguments.
                return None
            # Use the class 'alloc_opt_list' property to ensure we use the
            # correct class depending on whether 'cls' is associated with
            # Fortran2003 or Fortran2008.
            opts = cls.alloc_opt_list()(repmap(line[jdx + 1 :].lstrip()))
            line = line[:jdx].rstrip()
        return spec, Allocation_List(repmap(line)), opts

    @classmethod
    def alloc_opt_list(cls):
        """
        :returns: the Fortran2003 flavour of Alloc_Opt_List.
        :rtype: type
        """
        return Alloc_Opt_List

    def tostr(self):
        spec, lst, opts = self.items
        if spec is not None:
            if opts is not None:
                return "ALLOCATE(%s::%s, %s)" % (spec, lst, opts)
            else:
                return "ALLOCATE(%s::%s)" % (spec, lst)
        elif opts is not None:
            return "ALLOCATE(%s, %s)" % (lst, opts)
        else:
            return "ALLOCATE(%s)" % (lst)
