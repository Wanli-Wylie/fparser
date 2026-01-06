from fparser.common.splitline import string_replace_map
from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    Base,
)
from fparser.two.utils import (
    InternalError,
)

class Char_Literal_Constant(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R427::

        char-literal-constant is [ kind-param _ ] ' rep-char '
                              or [ kind-param _ ] " rep-char "
    """

    subclass_names = []
    rep = pattern.char_literal_constant

    @staticmethod
    def match(string):
        """
        Implements the matching for a Char_Literal_Constant. For example::

            "hello"
            'hello'
            nondefaultcharset_"nondefaultchars"

        There is an associated constraint C422: "The value of
        kind-param shall specify a representation method that exists
        on the processor." However, this cannot be validated by
        fparser so no checks are performed.

        :param str string: a string containing the code to match.

        :return: `None` if there is no match, otherwise a `tuple` of
                 size 2 containing the character constant and the kind
                 value as strings.
        :rtype: `NoneType` or (`str`, `NoneType`) or (`str`, `str`)

        """
        if not string:
            return None
        strip_string = string.strip()
        if not strip_string:
            # the string is empty or only contains blank space
            return None
        if strip_string[-1] not in "\"'":
            return None
        if strip_string[-1] == '"':
            abs_a_n_char_literal_constant_named = (
                pattern.abs_a_n_char_literal_constant_named2
            )
        else:
            abs_a_n_char_literal_constant_named = (
                pattern.abs_a_n_char_literal_constant_named1
            )
        line, repmap = string_replace_map(strip_string)
        match = abs_a_n_char_literal_constant_named.match(line)
        if not match:
            return None
        kind_param = match.group("kind_param")
        line = match.group("value")
        line = repmap(line)
        return line, kind_param

    def tostr(self):
        """
        :return: this Char_Literal_Constant as a string.
        :rtype: str

        :raises InternalError: if the internal items list variable is \
                not the expected size.
        :raises InternalError: if the first element of the internal \
                items list is None or is an empty string.
        """
        if len(self.items) != 2:
            raise InternalError(
                "Class Char_Literal_Constant method tostr() has '{0}' items, "
                "but expecting 2.".format(len(self.items))
            )
        if not self.items[0]:
            # items[0] is the value of the constant so is required. It
            # also can't be empty as it needs to include the
            # surrounding quotes to be valid
            raise InternalError(
                "Class Char_Literal_Constant method tostr(). 'Items' entry 0 "
                "should not be empty"
            )
        char_str = str(self.items[0])
        if not self.items[1]:
            return char_str
        # The character constant has a kind specifier
        kind_str = str(self.items[1])
        return f"{kind_str}_{char_str}"
