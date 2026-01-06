from fparser.two.utils import (
    Base,
)

class Interface_Specification(Base):  # R1202
    """
    ::

        <interface-specification> = <interface-body>
                                    | <procedure-stmt>

    """

    subclass_names = ["Interface_Body", "Procedure_Stmt"]
