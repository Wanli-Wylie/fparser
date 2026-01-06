from end_function_stmt import End_Function_Stmt
from function_stmt import Function_Stmt
from specification_part import Specification_Part

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
