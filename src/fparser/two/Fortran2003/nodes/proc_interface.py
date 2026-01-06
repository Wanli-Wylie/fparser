class Proc_Interface(Base):  # R1212
    """
    ::

        <proc-interface> = <interface-name>
                           | <declaration-type-spec>

    """

    subclass_names = ["Interface_Name", "Declaration_Type_Spec"]
