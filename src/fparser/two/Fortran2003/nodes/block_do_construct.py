class Block_Do_Construct(Base):  # pylint: disable=invalid-name
    """
    R826::

        <block-do-construct> = <block-label-do-construct>
                               | <block-nonlabel-do-construct>

    """

    subclass_names = ["Block_Label_Do_Construct", "Block_Nonlabel_Do_Construct"]
