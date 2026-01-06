from fparser.two.utils import (
    BlockBase,
)

from contains_stmt import Contains_Stmt
from module_subprogram import Module_Subprogram

class Module_Subprogram_Part(BlockBase):  # R1107
    """
    ::

        <module-subprogram-part> = <contains-stmt>
                                       <module-subprogram>
                                       [ <module-subprogram> ]...

    """

    subclass_names = []
    use_names = ["Contains_Stmt", "Module_Subprogram"]

    @staticmethod
    def match(reader):
        return BlockBase.match(Contains_Stmt, [Module_Subprogram], None, reader)
