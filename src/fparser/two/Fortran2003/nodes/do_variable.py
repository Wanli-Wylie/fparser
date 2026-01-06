from fparser.two.utils import (
    Base,
)

class Do_Variable(Base):  # pylint: disable=invalid-name
    """
    R831::

        <do-variable> = <scalar-int-variable>

    """

    subclass_names = ["Scalar_Int_Variable"]
