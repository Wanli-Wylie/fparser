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
