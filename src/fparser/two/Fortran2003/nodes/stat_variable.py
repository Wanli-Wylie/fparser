from fparser.two.utils import (
    Base,
)

class Stat_Variable(Base):  # R625
    """
    ::

        <stat-variable> = <scalar-int-variable>

    """

    subclass_names = ["Scalar_Int_Variable"]
