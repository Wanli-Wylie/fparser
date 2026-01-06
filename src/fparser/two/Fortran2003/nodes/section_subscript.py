class Section_Subscript(Base):  # R619
    """
    ::

        <section-subscript> = <subscript>
                              | <subscript-triplet>
                              | <vector-subscript>

    """

    subclass_names = ["Subscript_Triplet", "Vector_Subscript", "Subscript"]
