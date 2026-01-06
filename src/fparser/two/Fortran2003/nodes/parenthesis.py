class Parenthesis(BracketBase):
    """
    Part of Fortran 2003 rule R701::

        parenthesis = ( expr )

    """

    subclass_names = []
    use_names = ["Expr"]

    @staticmethod
    def match(string):
        """Implements the matching of round brackets surrounding an expression
        which is specified as one of the matches in R701.

        :param str string: Fortran code to check for a match.

        :returns: `None` if there is no match, or a 3-tuple containing \
            the left bracket, the matched expression and the right \
            bracket.
        :rtype: NoneType or (str, subclass of \
            :py:class:`fparser.two.utils.Base`, str)

        """
        return BracketBase.match("()", Expr, string)
