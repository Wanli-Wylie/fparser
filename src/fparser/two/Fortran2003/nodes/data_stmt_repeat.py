from fparser.two.utils import (
    Base,
)

class Data_Stmt_Repeat(Base):  # R531
    """
    ::

        <data-stmt-repeat> = <scalar-int-constant>
                             | <scalar-int-constant-subobject>

    """

    subclass_names = ["Scalar_Int_Constant", "Scalar_Int_Constant_Subobject"]
