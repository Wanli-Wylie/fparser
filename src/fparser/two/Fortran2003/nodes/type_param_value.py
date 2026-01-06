from fparser.two.utils import (
    StringBase,
)

class Type_Param_Value(StringBase):  # R402
    """
    Fortran 2003 Rule 402::

        <type-param-value> = <scalar-int-expr>
                           | *
                           | :
    """

    subclass_names = ["Scalar_Int_Expr"]
    use_names = []

    @staticmethod
    def match(string):
        return StringBase.match(["*", ":"], string)
