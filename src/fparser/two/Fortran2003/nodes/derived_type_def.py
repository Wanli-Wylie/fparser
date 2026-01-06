class Derived_Type_Def(BlockBase):  # R429
    """
    ::

        <derived-type-def> = <derived-type-stmt>
                               [ <type-param-def-stmt> ]...
                               [ <private-or-sequence> ]...
                               [ <component-part> ]
                               [ <type-bound-procedure-part> ]
                               <end-type-stmt>
    """

    subclass_names = []
    use_names = [
        "Derived_Type_Stmt",
        "Type_Param_Def_Stmt",
        "Private_Or_Sequence",
        "Component_Part",
        "Type_Bound_Procedure_Part",
        "End_Type_Stmt",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Derived_Type_Stmt,
            [
                Type_Param_Def_Stmt,
                Private_Or_Sequence,
                Component_Part,
                Type_Bound_Procedure_Part,
            ],
            End_Type_Stmt,
            reader,
            match_names=True,  # C431
        )
