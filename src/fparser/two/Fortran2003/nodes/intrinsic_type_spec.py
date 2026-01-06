from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    WORDClsBase,
)
from fparser.two.utils import (
    NoMatchError,
)

from char_selector import Char_Selector
from kind_selector import Kind_Selector

class Intrinsic_Type_Spec(WORDClsBase):  # R403
    """
    ::

        <intrinsic-type-spec> = INTEGER [ <kind-selector> ]
                                | REAL [ <kind-selector> ]
                                | DOUBLE COMPLEX
                                | COMPLEX [ <kind-selector> ]
                                | CHARACTER [ <char-selector> ]
                                | LOGICAL [ <kind-selector> ]
        Extensions:
                                | DOUBLE PRECISION
                                | BYTE
    """

    subclass_names = []
    use_names = ["Kind_Selector", "Char_Selector"]

    @staticmethod
    def match(string):
        for w, cls in [
            ("INTEGER", Kind_Selector),
            ("REAL", Kind_Selector),
            ("COMPLEX", Kind_Selector),
            ("LOGICAL", Kind_Selector),
            ("CHARACTER", Char_Selector),
            (pattern.abs_double_complex_name, None),
            (pattern.abs_double_precision_name, None),
            ("BYTE", None),
        ]:
            try:
                obj = WORDClsBase.match(w, cls, string)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None
