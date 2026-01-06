


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

class Designator(Base):  # R603
    """
    Fortran 2003 rule R603::

        designator is object-name
                   or array-element
                   or array-section
                   or structure-component
                   or substring

    """

    # At the moment some array section text, and all structure
    # component and substring text will match the array-element
    # rule. This is because the associated rule constraints
    # (e.g. C617, C618 and C619) and specification text (see note 6.6)
    # are not currently enforced. Note, these constraints can not be
    # enforced until issue #201 has been addressed.
    subclass_names = [
        "Object_Name",
        "Array_Element",
        "Array_Section",
        "Structure_Component",
        "Substring",
    ]
