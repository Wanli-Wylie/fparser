from end_subroutine_stmt import End_Subroutine_Stmt
from specification_part import Specification_Part
from subroutine_stmt import Subroutine_Stmt

class Subroutine_Body(BlockBase):
    """
    ::

        <subroutine-body> = <subroutine-stmt>
                            [ <specification-part> ]
                          <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = ["Subroutine_Stmt", "Specification_Part", "End_Subroutine_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Subroutine_Stmt, [Specification_Part], End_Subroutine_Stmt, reader
        )
