class Function_Subprogram(BlockBase):  # R1223
    """
    ::

        <function-subprogram> = <function-stmt>
                                   [ <specification-part> ]
                                   [ <execution-part> ]
                                   [ <internal-subprogram-part> ]
                                <end-function-stmt>

    """

    subclass_names = []
    use_names = [
        "Function_Stmt",
        "Specification_Part",
        "Execution_Part",
        "Internal_Subprogram_Part",
        "End_Function_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Function_Stmt,
            [Specification_Part, Execution_Part, Internal_Subprogram_Part],
            End_Function_Stmt,
            reader,
        )
