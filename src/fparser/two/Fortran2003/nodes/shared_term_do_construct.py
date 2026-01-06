class Shared_Term_Do_Construct(Base):  # R840
    """
    ::

        <shared-term-do-construct> = <outer-shared-do-construct>
                                     | <inner-shared-do-construct>

    """

    subclass_names = ["Outer_Shared_Do_Construct", "Inner_Shared_Do_Construct"]
