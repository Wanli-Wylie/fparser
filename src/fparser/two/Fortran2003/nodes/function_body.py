class Function_Body(BlockBase):
    """
    ::

        <function-body> = <function-stmt>
                            [ <specification-part> ]
                          <end-function-stmt>

    """

    subclass_names = []
    use_names = ["Function_Stmt", "Specification_Part", "End_Function_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Function_Stmt, [Specification_Part], End_Function_Stmt, reader
        )
