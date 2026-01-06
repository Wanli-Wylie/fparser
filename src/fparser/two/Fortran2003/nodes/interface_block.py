from fparser.two.utils import (
    BlockBase,
)

from end_interface_stmt import End_Interface_Stmt
from interface_specification import Interface_Specification
from interface_stmt import Interface_Stmt

class Interface_Block(BlockBase):  # R1201
    """
    ::

        <interface-block> = <interface-stmt>
                                [ <interface-specification> ]...
                                <end-interface-stmt>
    """

    subclass_names = []
    use_names = ["Interface_Stmt", "Interface_Specification", "End_Interface_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Interface_Stmt, [Interface_Specification], End_Interface_Stmt, reader
        )
