from execution_part_construct import Execution_Part_Construct

class Do_Body(BlockBase):  # R837
    """
    <do-body> = [ <execution-part-construct> ]...
    """

    subclass_names = []
    use_names = ["Execution_Part_Construct"]

    @staticmethod
    def match(string):
        return BlockBase.match(None, [Execution_Part_Construct], None, string)
