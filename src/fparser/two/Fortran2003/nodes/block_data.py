from block_data_stmt import Block_Data_Stmt
from end_block_data_stmt import End_Block_Data_Stmt
from specification_part import Specification_Part

class Block_Data(BlockBase):  # R1116
    """
    ::
        <block-data> = <block-data-stmt>
                           [ <specification-part> ]
                           <end-block-data-stmt>
    """

    subclass_names = []
    use_names = ["Block_Data_Stmt", "Specification_Part", "End_Block_Data_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Block_Data_Stmt, [Specification_Part], End_Block_Data_Stmt, reader
        )
