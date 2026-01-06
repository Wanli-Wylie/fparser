


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

from attr_spec import Attr_Spec_List
from declaration_type_spec import Declaration_Type_Spec
from entity_decl import Entity_Decl
from entity_decl import Entity_Decl_List
from intrinsic_type_spec import Intrinsic_Type_Spec

class Type_Declaration_Stmt(Type_Declaration_StmtBase):  # R501
    """
    Fortran 2003 rule 501::

        type-declaration-stmt is declaration-type-spec [
            [ , attr-spec ]... :: ] entity-decl-list

    Associated constraints are::

        C507 (R501)  The same attr-spec shall not appear more than once in a given
             type-declaration-stmt.
        C509 (R501)  An entity declared with the CLASS keyword shall be a dummy
             argument or have the ALLOCATABLE or POINTER attribute.
        C510 (R501)  An array that has the POINTER or ALLOCATABLE attribute shall
             be specified with an array-spec that is a deferred-shape-spec-list.
        C511 (R501)  An array-spec for an object-name that is a function result
             that does not have the ALLOCATABLE or POINTER attribute shall be an
             explicit-shape-spec-list.
        C512 (R501)  If the POINTER attribute is specified, the ALLOCATABLE,
             TARGET, EXTERNAL, or INTRINSIC attribute shall not be specified.
        C513 (R501)  If the TARGET attribute is specified, the POINTER, EXTERNAL,
             INTRINSIC, or PARAMETER attribute shall not be specified.
        C514 (R501)  The PARAMETER attribute shall not be specified for a dummy
             argument, a pointer, an allocatable entity, a function, or an object
             in a common block.
        C515 (R501)  The INTENT, VALUE, and OPTIONAL attributes may be specified
             only for dummy arguments.
        C516 (R501)  The INTENT attribute shall not be specified for a dummy
             procedure without the POINTER attribute.
        C517 (R501)  The SAVE attribute shall not be specified for an object that
             is in a common block, a dummy argument, a procedure, a function
             result, an automatic data object, or an object with the PARAMETER
             attribute.
        C519 (R501)  An entity in an entity-decl-list shall not have the EXTERNAL
             or INTRINSIC attribute specified unless it is a function.
        C522 (R501)  The initialization shall appear if the statement contains a
             PARAMETER attribute.
        C523 (R501)  If initialization appears, a double-colon separator shall
             appear before the entity-decl-list.
        C526 (R501)  If the VOLATILE attribute is specified, the PARAMETER,
             INTRINSIC, EXTERNAL, or INTENT(IN) attribute shall not be specified.
        C527 (R501)  If the VALUE attribute is specified, the PARAMETER, EXTERNAL,
             POINTER, ALLOCATABLE, DIMENSION, VOLATILE, INTENT(INOUT), or
             INTENT(OUT) attribute shall not be specified.
        C528 (R501)  If the VALUE attribute is specified, the length type
             parameter values shall be omitted or specified by initialization
             expressions.
        C529 (R501)  The VALUE attribute shall not be specified for a dummy
             procedure.
        C530 (R501)  The ALLOCATABLE, POINTER, or OPTIONAL attribute shall not be
             specified for adummy argument of a procedure that has
             aproc-language-binding-spec.
        C532 (R501)  If a language-binding-spec is specified, the entity declared
             shall be an interoperable variable.
        C533 (R501)  If a language-binding-spec with a NAME= specifier appears,
             the entity-decl-list shall consist of a single entity-decl.
        C534 (R503)  The PROTECTED attribute is permitted only in the
             specification part of a module.
        C535 (R501)  The PROTECTED attribute is permitted only for a procedure
             pointer or named variable that is not in a common block.
        C536 (R501)  If the PROTECTED attribute is specified, the EXTERNAL,
             INTRINSIC, or PARAMETER attribute shall not be specified.

    C507, C509-C517, C519, C522-C523, C526-C530, C532-C533, C535-C536 are
    currently not checked - issue #259.

    """

    subclass_names = []
    use_names = ["Declaration_Type_Spec", "Attr_Spec_List", "Entity_Decl_List"]

    @staticmethod
    def get_attr_spec_list_cls():
        """Return the type used to match the attr-spec-list

        This method allows to overwrite the type used in :py:meth:`match`
        in derived classes
        (e.g., :py:class:`fparser.two.Fortran2008.Type_Declaration_Stmt`).

        This cannot be implemented as an attribute because the relevant type
        :class:`Attr_Spec_List` is auto-generated at the end of the file
        using the :attr:`use_names` property of the class.

        """
        return Attr_Spec_List

    @staticmethod
    def add_to_symbol_table(result):
        """Capture the declared symbols in the symbol table of the current
        scoping region

        :param result: the declared type, attributes and entities or None
        :type result: `NoneType` or \
                (Declaration_Type_Spec, Attr_Spec_List or NoneType, \
                 Entity_Decl_List)
        """
        if result:
            # We matched a declaration - capture the declared symbols in the
            # symbol table of the current scoping region.
            table = SYMBOL_TABLES.current_scope

            if table and isinstance(result[0], Intrinsic_Type_Spec):
                # We have a definition of symbol(s) of intrinsic type
                decl_list = walk(result, Entity_Decl)
                for decl in decl_list:
                    # TODO #201 use an enumeration to specify the primitive
                    # type rather than a string.
                    table.add_data_symbol(decl.items[0].string, str(result[0]))
            # TODO #201 support symbols that are not of intrinsic type.

    @classmethod
    def match(cls, string):
        """
        Attempts to match the supplied string as a type declaration. If the
        match is successful the declared symbols are added to the symbol table
        of the current scope (if there is one).

        Note that this is implemented as a class method to allow parameterizing
        the type used to match attr-spec-list via :py:meth:`get_attr_spec_list_cls`.

        :param str string: the string to match.

        :returns: 3-tuple containing the matched declaration.
        :rtype: (Declaration_Type_Spec, Attr_Spec_List or NoneType, \
                 Entity_Decl_List)

        """
        result = Type_Declaration_StmtBase.match(
            Declaration_Type_Spec,
            cls.get_attr_spec_list_cls(),
            Entity_Decl_List,
            string,
        )
        cls.add_to_symbol_table(result)
        return result

    @staticmethod
    def match2(string):
        line, repmap = string_replace_map(string)
        i = line.find("::")
        if i != -1:
            j = line[:i].find(",")
            if j != -1:
                i = j
        else:
            if line[:6].upper() == "DOUBLE":
                m = re.search(r"\s[a-z_]", line[6:].lstrip(), re.I)
                if m is None:
                    return
                i = m.start() + len(line) - len(line[6:].lstrip())
            else:
                m = re.search(r"\s[a-z_]", line, re.I)
                if m is None:
                    return
                i = m.start()
        type_spec = Declaration_Type_Spec(repmap(line[:i].rstrip()))
        if type_spec is None:
            return
        line = line[i:].lstrip()
        if line.startswith(","):
            i = line.find("::")
            if i == -1:
                return
            attr_specs = Attr_Spec_List(repmap(line[1:i].strip()))
            if attr_specs is None:
                return
            line = line[i:]
        else:
            attr_specs = None
        if line.startswith("::"):
            line = line[2:].lstrip()
        entity_decls = Entity_Decl_List(repmap(line))
        if entity_decls is None:
            return
        return type_spec, attr_specs, entity_decls

    def tostr(self):
        if self.items[1] is None:
            return "%s :: %s" % (self.items[0], self.items[2])
        else:
            return "%s, %s :: %s" % self.items
