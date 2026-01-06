from fparser.two.utils import (
    Base,
)

class Use_Defined_Operator(Base):  # R1115
    """
    ::

        <use-defined-operator> = <defined-unary-op>
                                 | <defined-binary-op>

    """

    subclass_names = ["Defined_Unary_Op", "Defined_Binary_Op"]
