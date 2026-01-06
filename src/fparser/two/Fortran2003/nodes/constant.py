class Constant(Base):  # R305
    """
    ::

        <constant> = <literal-constant>
                     | <named-constant>
    """

    subclass_names = ["Literal_Constant", "Named_Constant"]
