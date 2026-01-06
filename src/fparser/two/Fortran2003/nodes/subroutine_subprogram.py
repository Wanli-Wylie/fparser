class Subroutine_Subprogram(BlockBase):  # R1231
    """
    ::

        <subroutine-subprogram> = <subroutine-stmt>
                                     [ <specification-part> ]
                                     [ <execution-part> ]
                                     [ <internal-subprogram-part> ]
                                  <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = [
        "Subroutine_Stmt",
        "Specification_Part",
        "Execution_Part",
        "Internal_Subprogram_Part",
        "End_Subroutine_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Subroutine_Stmt,
            [Specification_Part, Execution_Part, Internal_Subprogram_Part],
            End_Subroutine_Stmt,
            reader,
        )
