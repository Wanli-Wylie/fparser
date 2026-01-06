from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)
from fparser.two.utils import (
    NoMatchError,
    InternalError,
)

from forall_triplet_spec import Forall_Triplet_Spec_List
from mask_expr import Scalar_Mask_Expr

class Forall_Header(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R754::

        forall-header is ( forall-triplet-spec-list [, scalar-mask-expr ] )

    """

    subclass_names = []
    use_names = ["Forall_Triplet_Spec_List", "Scalar_Mask_Expr"]

    @staticmethod
    def match(string):
        """Implements the matching for a Forall_Header.

        :param str string: A string containing the code to match.
        :return: `None` if there is no match, otherwise a `tuple` of \
                 size 2 containing a class of type \
                 `Forall_Triplet_Spec_List` and a class of type \
                 `Scalar_Mask_Expr` if there is a scalar mask \
                 expresssion and `None` if not.
        :rtype: (`Forall_Triplet_Spec_List`, `Scalar_Mask_Expr`) or \
                (`Forall_Triplet_Spec_List`, `None`) or `None`

        """
        strip_string = string.strip()
        if not strip_string:
            # Input only contains white space
            return None
        if strip_string[0] + strip_string[-1] != "()":
            # Input does not start with '(' and end with ')'
            return None
        strip_string_nobr = strip_string[1:-1].strip()
        try:
            # first try to match without a scalar mask expression
            return Forall_Triplet_Spec_List(strip_string_nobr), None
        except NoMatchError:
            # The match failed so try to match with the optional
            # scalar mask expression. Use repmap to remove any
            # unexpected "," e.g. an array access a(i,j), when
            # splitting the string.
            mapped_string, repmap = string_replace_map(strip_string_nobr)
            split_string = mapped_string.rsplit(",", 1)
            if len(split_string) != 2:
                return None
            left_str = repmap(split_string[0].rstrip())
            right_str = repmap(split_string[1].lstrip())
            return (Forall_Triplet_Spec_List(left_str), Scalar_Mask_Expr(right_str))

    def tostr(self):
        """:return: this Forall Header as a string
        :rtype: str
        :raises InternalError: if the length of the internal items \
        list is not 2.
        :raises InternalError: if the first entry of the internal \
        items list has no content, as a Forall_Triplet_List is \
        expected.

        """
        if len(self.items) != 2:
            raise InternalError(
                "Forall_Header.tostr(). 'items' should be of size 2 but "
                "found '{0}'.".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "Forall_Header.tostr(). 'items[0]' should be a "
                "Forall_Triplet_Spec_List instance but it is empty."
            )
        if not self.items[1]:
            # there is no scalar mask expression
            return "({0})".format(self.items[0])
        return "({0}, {1})".format(self.items[0], self.items[1])
