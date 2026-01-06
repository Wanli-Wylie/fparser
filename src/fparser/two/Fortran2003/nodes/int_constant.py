from fparser.two.utils import (
    Base,
)

class Int_Constant(Base):  # R308
    """
    ::

        <int-constant> = <constant>
    """

    subclass_names = ["Constant"]


class Scalar_Int_Constant(Base):
    subclass_names = ["Int_Constant"]
