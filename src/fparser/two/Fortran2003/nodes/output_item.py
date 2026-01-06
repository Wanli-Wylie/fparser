class Output_Item(Base):  # R916
    """
    ::

        <output-item> = <expr>
                        | <io-implied-do>
    """

    subclass_names = ["Expr", "Io_Implied_Do"]
