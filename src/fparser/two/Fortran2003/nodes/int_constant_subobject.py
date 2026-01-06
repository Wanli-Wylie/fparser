class Int_Constant_Subobject(Base):  # R533
    """
    Fortran 2003 Rule R533::

        <int-constant-subobject> = <constant-subobject>

    """

    subclass_names = ["Constant_Subobject"]


class Scalar_Int_Constant_Subobject(Base):
    subclass_names = ["Int_Constant_Subobject"]
