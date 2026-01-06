from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    STRINGBase,
)

class Defined_Op(STRINGBase):  # pylint: disable=invalid-name
    """
    Utility class that Implements the functionality of rules R703 and
    R723 (as the rules are the same)::

        defined-op is . letter [ letter ]... .

    C704 (R723) A defined-binary-op shall not contain more than 63
    letters and shall not be the same as any intrinsic-operator or
    logical-literal-constant.

    C704 (R703) A defined-unary-op shall not contain more than 63
    letters and shall not be the same as any intrinsic-operator or
    logical-literal-constant.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """Implements the matching for a (user) Defined Unary or Binary
        Operator.

        :param str string: Fortran code to check for a match
        :return: `None` if there is no match, or a tuple containing \
                 the matched operator as a string
        :rtype: None or (str)

        """
        strip_string = string.strip()
        if len(strip_string) > 65:
            # C704. Must be 63 letters or fewer (Test for >65 due
            # to the two dots).
            return None
        if pattern.non_defined_binary_op.match(strip_string):
            # C704. Must not match with an intrinsic-operator or
            # logical-literal-constant
            return None
        return STRINGBase.match(pattern.abs_defined_op, strip_string)
