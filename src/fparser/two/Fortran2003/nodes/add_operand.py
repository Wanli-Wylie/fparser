from mult_operand import Mult_Operand

class Add_Operand(BinaryOpBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R705::

        add-operand is [ add-operand mult-op ] mult-operand

    Rule R705 is implemented in two parts, the first with the optional
    part included (in the match method for this class) and the second
    without the optional part (specified in subclass_names).

    Note rule R708 (mult-op is * or /) is implemented directly here as
    the mult_op pattern.

    There is potential to accidentally match a sign in an exponent as the
    plus/minus sign in a level-2-expr. If this were to happen then it is
    possible to end up matching a * or / (a level 1 expression) before
    matching a valid + or - which would normally result in no match
    overall as * or / are matched after + or -. This situation is
    avoided by tokenising the string before performing the match so
    that any numerical constants involving exponents are replaced by
    simple symbols. (The tokenisation is performed by
    `fparser.common.splitline.string_replace_map`.)

    """

    subclass_names = ["Mult_Operand"]
    use_names = ["Mult_Operand"]

    @staticmethod
    def match(string):
        """Implement the matching for the add-operand rule. Makes use of the
        pre-defined mult_op pattern and the BinaryOpBase baseclass.

        :param str string: the string to match.

        :returns: a tuple of size 3 containing an fparser2 class \
            instance matching a level-2-expr expression, a string \
            containing the matched operator and an fparser2 class \
            instance matching a mult-operand if there is a match, or \
            None if there is not.
        :rtype: (subclass of :py:class:`fparser.two.utils.Base`, str, \
            subclass of :py:class:`fparser.two.utils.Base`) or NoneType

        """
        return BinaryOpBase.match(
            Add_Operand, pattern.mult_op.named(), Mult_Operand, string
        )
