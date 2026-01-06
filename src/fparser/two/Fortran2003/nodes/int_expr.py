from binary_constant import Binary_Constant
from char_literal_constant import Char_Literal_Constant
from complex_literal_constant import Complex_Literal_Constant
from expr import Expr
from hex_constant import Hex_Constant
from logical_literal_constant import Logical_Literal_Constant
from octal_constant import Octal_Constant
from real_literal_constant import Real_Literal_Constant
from signed_real_literal_constant import Signed_Real_Literal_Constant

class Int_Expr(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R727::

        int-expr is expr

    C708 int-expr shall be of type integer.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """Implements the matching for an integer expression.

        :param str string: Fortran code to check for a match.
        :returns: `None` if there is no match, or an fparser2 class \
                  instance containing the matched expression.
        :rtype: NoneType or :py:class:`fparser.two.utils.Base`

        """
        excluded = (
            Binary_Constant,
            Octal_Constant,
            Hex_Constant,
            Signed_Real_Literal_Constant,
            Real_Literal_Constant,
            Complex_Literal_Constant,
            Char_Literal_Constant,
            Logical_Literal_Constant,
        )
        # Attempt to match as a general expression.
        result = Expr(string)
        # C708: the match should fail if the result is not an integer
        # expression. This is difficult to check in general so for the
        # time being check that, in the case where a literal constant
        # is returned, this is not of the wrong type.
        if isinstance(result, excluded):
            return None
        return result


class Scalar_Int_Expr(Base):
    subclass_names = ["Int_Expr"]
