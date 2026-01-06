from fparser.two.utils import (
    Base,
)

class M(Base):  # R1007
    """
    ::

        m = int-literal-constant

    Subject to the constraint::

        C1007: m is without kind parameters.

    """

    subclass_names = ["Int_Literal_Constant"]
