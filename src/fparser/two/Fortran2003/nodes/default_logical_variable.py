class Default_Logical_Variable(Base):  # R605
    """
    ::

        <default-logical-variable> = <variable>

    """

    subclass_names = ["Variable"]


class Scalar_Default_Logical_Variable(Base):
    subclass_names = ["Default_Logical_Variable"]
