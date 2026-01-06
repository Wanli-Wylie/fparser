from fparser.two.utils import (
    Base,
)

class Constant(Base):  # R305
    """
    ::

        <constant> = <literal-constant>
                     | <named-constant>
    """

    subclass_names = ["Literal_Constant", "Named_Constant"]


class Scalar_Constant(Base):
    subclass_names = ["Constant"]
