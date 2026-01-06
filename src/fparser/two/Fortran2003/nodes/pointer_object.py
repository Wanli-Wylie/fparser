class Pointer_Object(Base):  # R634
    """
    ::

        <pointer-object> = <variable-name>
                           | <structure-component>
                           | <proc-pointer-name>

    """

    subclass_names = ["Variable_Name", "Structure_Component", "Proc_Pointer_Name"]
