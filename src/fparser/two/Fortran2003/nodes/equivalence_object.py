class Equivalence_Object(Base):  # R556
    """
    ::

        <equivalence-object> = <variable-name>
                               | <array-element>
                               | <substring>

    """

    subclass_names = ["Variable_Name", "Array_Element", "Substring"]
