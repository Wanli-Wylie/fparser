from fparser.two.utils import (
    Base,
)

class Declaration_Construct(Base):  # R207
    """
    Fortran 2003 rule R207::

        declaration-construct is derived-type-def
                               or entry-stmt
                               or enum-def
                               or format-stmt
                               or interface-block
                               or parameter-stmt
                               or procedure-declaration-stmt
                               or specification-stmt
                               or type-declaration-stmt
                               or stmt-function-stmt

    Note, stmt-function-stmt is not currently matched.

    """

    # Commented out Stmt_Function_Stmt as it can falsely match an
    # access to an array or function. Reintroducing statement
    # functions is captured in issue #202.

    #                   'Type_Declaration_Stmt', 'Stmt_Function_Stmt']
    subclass_names = [
        "Derived_Type_Def",
        "Entry_Stmt",
        "Enum_Def",
        "Format_Stmt",
        "Interface_Block",
        "Parameter_Stmt",
        "Procedure_Declaration_Stmt",
        "Specification_Stmt",
        "Type_Declaration_Stmt",
    ]
