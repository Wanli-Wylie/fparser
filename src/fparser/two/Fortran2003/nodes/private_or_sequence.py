class Private_Or_Sequence(Base):  # R432
    """
    ::

        <private-or-sequence> = <private-components-stmt>
                                | <sequence-stmt>

    """

    subclass_names = ["Private_Components_Stmt", "Sequence_Stmt"]
