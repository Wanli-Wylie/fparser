class Program_Unit(Base):  # R202
    """
    Fortran 2003 Rule R202::

        <program-unit> = <main-program>
                         | <external-subprogram>
                         | <module>
                         | <block-data>
    """

    subclass_names = [
        "Comment",
        "Main_Program",
        "External_Subprogram",
        "Module",
        "Block_Data",
    ]
