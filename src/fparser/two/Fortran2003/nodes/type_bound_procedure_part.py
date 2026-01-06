from fparser.two.utils import (
    BlockBase,
)

from binding_private_stmt import Binding_Private_Stmt
from contains_stmt import Contains_Stmt
from proc_binding_stmt import Proc_Binding_Stmt

class Type_Bound_Procedure_Part(BlockBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R448.

    Specifies the type-bound procedure part of a derived type::

        type-bound-procedure-part is contains-stmt
                                          [ binding-private-stmt ]
                                          proc-binding-stmt
                                          [ proc-binding-stmt ]...

    """

    subclass_names = []
    use_names = ["Contains_Stmt", "Binding_Private_Stmt", "Proc_Binding_Stmt"]

    @staticmethod
    def match(reader):
        """
        :param reader: the Fortran reader containing the line(s) of code \
        that we are trying to match
        :type reader: :py:class:`fparser.common.readfortran.FortranReaderBase`

        :return: code block containing instances of the classes that match \
                 the syntax of the type-bound procedure part of a derived type.
        :rtype: ([`Contains_Stmt`, `Specific_Binding`, `str`, `Name`, \
                  `Name`]) or `None`
        """
        return BlockBase.match(
            Contains_Stmt, [Binding_Private_Stmt, Proc_Binding_Stmt], None, reader
        )
