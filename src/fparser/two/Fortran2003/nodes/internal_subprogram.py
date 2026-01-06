class Internal_Subprogram(Base):  # R211
    """
    ::

        <internal-subprogram> = <function-subprogram>
                                | <subroutine-subprogram>

    """

    subclass_names = ["Function_Subprogram", "Subroutine_Subprogram"]
