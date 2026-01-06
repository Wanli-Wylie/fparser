class Designator(Base):  # R603
    """
    Fortran 2003 rule R603::

        designator is object-name
                   or array-element
                   or array-section
                   or structure-component
                   or substring

    """

    # At the moment some array section text, and all structure
    # component and substring text will match the array-element
    # rule. This is because the associated rule constraints
    # (e.g. C617, C618 and C619) and specification text (see note 6.6)
    # are not currently enforced. Note, these constraints can not be
    # enforced until issue #201 has been addressed.
    subclass_names = [
        "Object_Name",
        "Array_Element",
        "Array_Section",
        "Structure_Component",
        "Substring",
    ]
