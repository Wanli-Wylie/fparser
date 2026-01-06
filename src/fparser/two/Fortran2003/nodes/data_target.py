class Data_Target(Base):  # R739
    """
    ::

        <data-target> = <variable>
                        | <expr>

    """

    subclass_names = ["Variable", "Expr"]
