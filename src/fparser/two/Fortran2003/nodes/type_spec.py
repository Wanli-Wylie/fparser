from fparser.two.utils import (
    Base,
)

class Type_Spec(Base):  # R401
    """
    ::
        <type-spec> = <intrinsic-type-spec>
                      | <derived-type-spec>
    """

    subclass_names = ["Intrinsic_Type_Spec", "Derived_Type_Spec"]
