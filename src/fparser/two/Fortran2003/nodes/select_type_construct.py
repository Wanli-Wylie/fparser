from end_select_type_stmt import End_Select_Type_Stmt
from execution_part_construct import Execution_Part_Construct
from select_type_stmt import Select_Type_Stmt
from type_guard_stmt import Type_Guard_Stmt

class Select_Type_Construct(BlockBase):  # R821
    """
    ::

        <select-type-construct> = <select-type-stmt>
                                      [ <type-guard-stmt>
                                        <block> == [<execution-part-construct>]..
                                      ]...
                                      <end-select-type-stmt>

    """

    subclass_names = []
    use_names = [
        "Select_Type_Stmt",
        "Type_Guard_Stmt",
        "Execution_Part_Construct",
        "End_Select_Type_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Select_Type_Stmt,
            [Type_Guard_Stmt, Execution_Part_Construct, Type_Guard_Stmt],
            End_Select_Type_Stmt,
            reader,
            match_names=True,  # C819
            strict_match_names=True,  # C819
            match_name_classes=(Type_Guard_Stmt),
        )
