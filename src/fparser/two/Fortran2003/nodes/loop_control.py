from do_variable import Do_Variable
from int_expr import Scalar_Int_Expr
from logical_expr import Scalar_Logical_Expr

class Loop_Control(Base):  # R830
    """
    Fortran 2003 rule R830

    loop-control is [ , ] do-variable = scalar-int-expr , scalar-int-expr
                       [ , scalar-int-expr ]
                    or [ , ] WHILE ( scalar-logical-expr )

    This class would be better and more extensible if it called 2
    classes, one for each of the above expressions. Something like the
    suggestion below. However, this would result in a different
    fparser tree, see issue #416.

    F2003: While_Loop_Cntl: scalar-logical-expression, delim
    F2003: Counter_Loop_Cntl: var, lower, upper, [step], delim
    F2008: Concurrent_Loop_Cntl: conc_expr, delim
    F2018: Concurrent_Loop_Cntl: conc_expr, local_x, delim

    """

    subclass_names = []
    use_names = ["Do_Variable", "Scalar_Int_Expr", "Scalar_Logical_Expr"]

    @staticmethod
    def match(string):
        """Attempts to match the supplied text with this rule.

        :param str string: Fortran code to check for a match.

        :returns: None if there is no match, a 3-tuple with the first \
            entry providing the result of matching the 'WHILE' part of \
            the rule if there is a match, the second entry providing \
            the result of matching the 'COUNTER' part of the rule if \
            there is a match and the third entry indicating whether \
            there is an optional preceding ','.
        :rtype: Optional[Tuple[ \
            Optional[ \
                :py:class:`fparser.two.Fortran2003.Scalar_Logical_Expr`], \
            Optional[Tuple[ \
                :py:class:`fparser.two.Fortran2003.Do_Variable`, List[str]]], \
            Optional[str]]]

        """
        line = string.lstrip().rstrip()
        # Try to match optional delimiter
        optional_delim = None
        if line.startswith(","):
            line = line[1:].lstrip()
            optional_delim = ","
        line, repmap = string_replace_map(line)
        # Try to match with WHILE
        if line[:5].upper() == "WHILE" and line[5:].lstrip().startswith("("):
            brackets = line[5:].lstrip()
            rbrack_index = brackets.find(")")
            if rbrack_index != -1 and rbrack_index == len(brackets) - 1:
                scalar_logical_expr = Scalar_Logical_Expr(
                    repmap(brackets[1:rbrack_index].strip())
                )
                return (scalar_logical_expr, None, optional_delim)
        # Try to match counter expression
        # More than one '=' in counter expression is not valid
        if line.count("=") != 1:
            return None
        var, rhs = line.split("=")
        rhs = [entry.strip() for entry in rhs.lstrip().split(",")]
        # Incorrect number of elements in counter expression
        if not 2 <= len(rhs) <= 3:
            return None
        counter_expr = (
            Do_Variable(repmap(var.rstrip())),
            list(map(Scalar_Int_Expr, list(map(repmap, rhs)))),
        )
        return (None, counter_expr, optional_delim)

    def tostr(self):
        """
        :returns: the Fortran representation of this object.
        :rtype: str
        """
        if self.items[0]:
            # Return loop control construct containing "WHILE" condition and
            # its <scalar-logical-expr>
            loopctrl = f"WHILE ({self.items[0]})"
        else:  # counter expression
            # Return loop control construct containing counter expression:
            # <do-variable> as LHS and <scalar-int-expr> list as RHS
            loopctrl = (
                f"{self.items[1][0]} = " f"{', '.join(map(str, self.items[1][1]))}"
            )
        # Add optional delimiter to loop control construct if present
        if self.items[2]:
            loopctrl = f"{self.items[2]} {loopctrl}"
        return loopctrl
