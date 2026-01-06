class Block(BlockBase):  # R801
    """
    <block> = [ <execution-part-construct> ]...
    """

    subclass_names = []
    use_names = ["Execution_Part_Construct"]

    @staticmethod
    def match(string):
        return BlockBase.match(None, [Execution_Part_Construct], None, string)
