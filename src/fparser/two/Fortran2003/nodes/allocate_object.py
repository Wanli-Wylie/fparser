class Allocate_Object(Base):  # R629
    """
    ::

        <allocate-object> = <variable-name>
                            | <structure-component>

    """

    subclass_names = ["Variable_Name", "Structure_Component"]
