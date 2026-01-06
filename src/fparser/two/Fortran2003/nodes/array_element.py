from fparser.two.utils import (
    Base,
)

class Array_Element(Base):  # R616
    """
    ::

        <array-element> = <data-ref>

    """

    subclass_names = ["Data_Ref"]
