class Constant_Subobject(Base):  # R534
    """
    Fortran 2003 Rule R534::

        <constant-subobject> = <designator>

    """

    subclass_names = ["Designator"]


class Scalar_Constant_Subobject(Base):
    subclass_names = ["Constant_Subobject"]
