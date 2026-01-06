class Array_Spec(Base):  # R510
    """
    Fortran2003 Rule R510::

        <array-spec> = <explicit-shape-spec-list>
                       | <assumed-shape-spec-list>
                       | <deferred-shape-spec-list>
                       | <assumed-size-spec>

    """

    subclass_names = [
        "Assumed_Size_Spec",
        "Explicit_Shape_Spec_List",
        "Assumed_Shape_Spec_List",
        "Deferred_Shape_Spec_List",
    ]
