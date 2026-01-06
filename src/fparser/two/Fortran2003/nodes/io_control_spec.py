from fparser.two.utils import (
    KeywordValueBase,
)

from default_char_expr import Scalar_Default_Char_Expr
from format import Format
from int_expr import Scalar_Int_Expr
from int_variable import Scalar_Int_Variable
from io_unit import Io_Unit
from iomsg_variable import Iomsg_Variable
from label import Label
from name import Namelist_Group_Name
from scalar_char_initialization_expr import Scalar_Char_Initialization_Expr

class Io_Control_Spec(KeywordValueBase):
    """
    This class implements *partial* support for Rule 913::

        <io-control-spec> is  [UNIT = ] <io-unit>
                            | [ FMT = ] <format>
                            | [ NML = ] <namelist-group-name>
                            | ADVANCE = <scalar-default-char-expr>
                            | ASYNCHRONOUS = <scalar-char-initialization-expr>
                            | BLANK = <scalar-default-char-expr>
                            | DECIMAL = <scalar-default-char-expr>
                            | DELIM = <scalar-default-char-expr>
                            | END = <label>
                            | EOR = <label>
                            | ERR = <label>
                            | ID = <scalar-int-variable>
                            | IOMSG = <iomsg-variable>
                            | IOSTAT = <scalar-int-variable>
                            | PAD = <scalar-default-char-expr>
                            | POS = <scalar-int-expr>
                            | REC = <scalar-int-expr>
                            | ROUND = <scalar-default-char-expr>
                            | SIGN = <scalar-default-char-expr>
                            | SIZE = <scalar-int-variable>

    The support is partial because this class requires that every spec be
    named. The specs that may not be named are explicitly handled in
    Io_Control_Spec_List.match().

    """

    subclass_names = []
    use_names = [
        "Io_Unit",
        "Format",
        "Namelist_Group_Name",
        "Scalar_Default_Char_Expr",
        "Scalar_Char_Initialization_Expr",
        "Label",
        "Scalar_Int_Variable",
        "Iomsg_Variable",
        "Scalar_Int_Expr",
    ]

    @staticmethod
    def match(string):
        for k, v in [
            ("UNIT", Io_Unit),
            ("FMT", Format),
            ("NML", Namelist_Group_Name),
            (
                ["ADVANCE", "BLANK", "DECIMAL", "DELIM", "PAD", "ROUND", "SIGN"],
                Scalar_Default_Char_Expr,
            ),
            ("ASYNCHRONOUS", Scalar_Char_Initialization_Expr),
            (["END", "EOR", "ERR"], Label),
            (["ID", "IOSTAT", "SIZE"], Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            (["POS", "REC"], Scalar_Int_Expr),
        ]:
            obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            if obj:
                return obj
        return None
