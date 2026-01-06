from fparser.two.utils import (
    BlockBase,
)

from end_do import End_Do
from execution_part_construct import Execution_Part_Construct
from label_do_stmt import Label_Do_Stmt

class Block_Label_Do_Construct(BlockBase):  # pylint: disable=invalid-name
    """
    R826_1::

        <block-label-do-construct> = <label-do-stmt>
                                       [ <execution-part-construct> ]...
                                       <end-do>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Execution_Part_Construct", "End_Do"]

    @classmethod
    def match(cls, reader):
        """
        :param reader: instance of `FortranReaderBase` class
        :type reader: :py:class:`FortranReaderBase`
        :return: code block matching the labeled "DO" construct
        :rtype: string
        """
        return BlockBase.match(
            cls.label_do_stmt_cls(),
            [Execution_Part_Construct],
            End_Do,
            reader,
            match_labels=True,
            enable_do_label_construct_hook=True,
        )

    @staticmethod
    def label_do_stmt_cls():
        """
        :returns: Fortran2003 Label_Do_Stmt class.
        :rtype: :py:class:`fparser.two.Fortran2003.Label_Do_Stmt`

        """
        return Label_Do_Stmt

    def tofortran(self, tab="", isfix=None):
        """
        :param str tab: tab character or empty string.
        :param bool isfix: whether the reader is in fixed format.

        :return: parsed representation of the labeled "DO" construct.
        :rtype: str
        """
        lblock = []
        start = self.content[0]
        end = self.content[-1]
        extra_tab = "  "
        lblock.append(start.tofortran(tab=tab, isfix=isfix))
        for item in self.content[1:-1]:
            lblock.append(item.tofortran(tab=tab + extra_tab, isfix=isfix))
        if len(self.content) > 1:
            lblock.append(end.tofortran(tab=tab, isfix=isfix))
        return "\n".join(lblock)
