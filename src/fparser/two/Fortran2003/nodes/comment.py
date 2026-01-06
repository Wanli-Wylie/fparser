


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

class Comment(Base):
    """
    Represents a Fortran Comment.
    """

    subclass_names = []

    @show_result
    def __new__(cls, string, parent_cls=None):
        """
        Create a new Comment instance.

        :param type cls: the class of object to create.
        :param string: (source of) Fortran string to parse.
        :type string: str or :py:class:`FortranReaderBase`
        :param parent_cls: the parent class of this object.
        :type parent_cls: :py:type:`type`

        """
        from fparser.common import readfortran

        if isinstance(string, readfortran.Comment):
            # We were after a comment and we got a comment. Construct
            # one manually to avoid recursively calling this __new__
            # method again...
            obj = object.__new__(cls)
            obj.init(string)
            return obj
        elif isinstance(string, FortranReaderBase):
            reader = string
            item = reader.get_item()
            if item is None:
                return
            if isinstance(item, readfortran.Comment):
                # This effectively recursively calls this routine
                return Comment(item)
            else:
                # We didn't get a comment so put the item back in the FIFO
                reader.put_item(item)
                return
        else:
            # We didn't get a comment
            return

    def init(self, comment):
        """
        Initialise this Comment

        :param  comment: The comment object produced by the reader
        :type comment: :py:class:`readfortran.Comment`
        """
        self.items = [comment.comment]
        self.item = comment

    def tostr(self):
        """
        :returns: this comment as a string.
        :rtype: :py:class:`str`
        """
        return str(self.items[0])
