from end_module_stmt import End_Module_Stmt
from module_stmt import Module_Stmt
from module_subprogram_part import Module_Subprogram_Part
from specification_part import Specification_Part

class Module(BlockBase):  # R1104
    """
    ::

        <module> = <module-stmt>
                       [ <specification-part> ]
                       [ <module-subprogram-part> ]
                       <end-module-stmt>

    """

    subclass_names = []
    use_names = [
        "Module_Stmt",
        "Specification_Part",
        "Module_Subprogram_Part",
        "End_Module_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Module_Stmt,
            [Specification_Part, Module_Subprogram_Part],
            End_Module_Stmt,
            reader,
        )
