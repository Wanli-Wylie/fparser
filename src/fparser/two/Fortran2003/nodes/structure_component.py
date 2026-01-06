from fparser.two.utils import (
    Base,
)

class Structure_Component(Base):  # R614
    """
    ::

        <structure-component> = <data-ref>

    """

    subclass_names = ["Data_Ref"]


class Scalar_Structure_Component(Base):
    subclass_names = ["Structure_Component"]
