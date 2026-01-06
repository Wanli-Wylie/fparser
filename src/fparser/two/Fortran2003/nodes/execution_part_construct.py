from fparser.two.utils import (
    Base,
)

class Execution_Part_Construct(Base):  # R209
    """
    ::

        <execution-part-construct> = <executable-construct>
                                     | <format-stmt>
                                     | <entry-stmt>
                                     | <data-stmt>

    """

    subclass_names = [
        "Comment",
        "Executable_Construct",
        "Format_Stmt",
        "Entry_Stmt",
        "Data_Stmt",
    ]
