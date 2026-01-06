class Implicit_Part_Stmt(Base):  # R206
    """
    Fortran2003 Rule R206::

        <implicit-part-stmt> = <implicit-stmt>
                               | <parameter-stmt>
                               | <format-stmt>
                               | <entry-stmt>
    """

    subclass_names = [
        "Comment",
        "Implicit_Stmt",
        "Parameter_Stmt",
        "Format_Stmt",
        "Entry_Stmt",
    ]
