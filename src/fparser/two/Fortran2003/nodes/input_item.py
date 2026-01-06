class Input_Item(Base):  # R915
    """
    ::

        <input-item> = <variable>
                       | <io-implied-do>

    """

    subclass_names = ["Variable", "Io_Implied_Do"]
