from associate_stmt import Associate_Stmt
from end_associate_stmt import End_Associate_Stmt
from execution_part_construct import Execution_Part_Construct

class Associate_Construct(BlockBase):  # R816
    """
    ::

        <associate-construct> = <associate-stmt>
                                    <block> == [ <execution-part-construct> ]...
                                    <end-associate-stmt>

    """

    subclass_names = []
    use_names = ["Associate_Stmt", "Execution_Part_Construct", "End_Associate_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Associate_Stmt,
            [Execution_Part_Construct],
            End_Associate_Stmt,
            reader,
            match_names=True,  # C810
            strict_match_names=True,  # C810
        )
