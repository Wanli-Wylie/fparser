class Access_Id(Base):  # R519
    """
    Fortran2003 Rule R519::

        <access-id> = <use-name>
                      | <generic-spec>

    """

    subclass_names = ["Use_Name", "Generic_Spec"]
