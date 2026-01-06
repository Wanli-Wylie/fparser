from fparser.two.utils import (
    Base,
)

class Internal_File_Variable(Base):  # R903
    """
    ::

        <internal-file-variable> = <char-variable>

    C901 -  <char-variable> shall not be an array section with a
    vector subscript.

    """

    subclass_names = ["Char_Variable"]
