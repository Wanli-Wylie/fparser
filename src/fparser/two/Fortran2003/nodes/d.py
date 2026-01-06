from fparser.two.utils import (
    Base,
)

class D(Base):  # R1008
    """
    ::

        d = int-literal-constant

    Subject to the constraint::

        C1007: d is without kind parameters.

    """

    subclass_names = ["Int_Literal_Constant"]
