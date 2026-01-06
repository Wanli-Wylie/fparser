class Io_Implied_Do_Object(Base):  # R918
    """
    ::

        <io-implied-do-object> = <input-item>
                                 | <output-item>

    """

    subclass_names = ["Input_Item", "Output_Item"]
