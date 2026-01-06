from fparser.two.utils import (
    Base,
)

class Char_String_Edit_Desc(Base):  # R1019
    """
    <char-string-edit-desc> = <char-literal-constant>
    """

    subclass_names = ["Char_Literal_Constant"]
