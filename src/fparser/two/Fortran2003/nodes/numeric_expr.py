class Numeric_Expr(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R728::

        numeric-expr is expr

    C709 numeric-expr shall be of type integer, real or complex.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """Implements the matching for a numeric expression.

        :param str string: Fortran code to check for a match.
        :returns: `None` if there is no match, or an fparser2 class \
                  instance containing the matched expression.
        :rtype: NoneType or :py:class:`fparser.two.utils.Base`

        """
        excluded = (
            Binary_Constant,
            Octal_Constant,
            Hex_Constant,
            Char_Literal_Constant,
            Logical_Literal_Constant,
        )
        # Attempt to match as a general expression.
        result = Expr(string)
        # C709: the match should fail if the result is not an integer,
        # real or complex expression. This is difficult to check in
        # general so for the time being check that, in the case where
        # a literal constant is returned, this is not of the wrong
        # type.
        if isinstance(result, excluded):
            return None
        return result
