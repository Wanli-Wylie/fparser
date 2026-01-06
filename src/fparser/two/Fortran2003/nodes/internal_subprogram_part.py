from fparser.two.utils import (
    BlockBase,
)

from contains_stmt import Contains_Stmt
from internal_subprogram import Internal_Subprogram

class Internal_Subprogram_Part(BlockBase):  # R210
    """
    ::

        <internal-subprogram-part> = <contains-stmt>
                                       <internal-subprogram>
                                       [ <internal-subprogram> ]...

    """

    subclass_names = []
    use_names = ["Contains_Stmt", "Internal_Subprogram"]

    @staticmethod
    def match(reader):
        return BlockBase.match(Contains_Stmt, [Internal_Subprogram], None, reader)
