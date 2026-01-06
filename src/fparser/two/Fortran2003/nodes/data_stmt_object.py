class Data_Stmt_Object(Base):  # R526
    """
    Fortran 2003 Rule R526::

        <data-stmt-object> = <variable>
                             | <data-implied-do>

    """

    subclass_names = ["Variable", "Data_Implied_Do"]
