


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

class Cray_Pointee_Array_Spec(Base):  # pylint: disable=invalid-name
    """
    ::

        cray-pointee-array-spec is explicit-shape-spec-list
                                or assumed-size-spec

    The above two forms of declaration are the only ones allowed
    according to
    `<http://pubs.cray.com/content/S-3901/8.6/
    cray-fortran-reference-manual-s-3901-86/types>`_ or
    `<https://docs.oracle.com/cd/E19957-01/805-4941/z40000a54ba7/index.html>`_

    """

    subclass_names = ["Assumed_Size_Spec", "Explicit_Shape_Spec_List"]
