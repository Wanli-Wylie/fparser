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
