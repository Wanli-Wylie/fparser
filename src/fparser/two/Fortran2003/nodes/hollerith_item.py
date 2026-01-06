import re


from fparser.two.utils import (
    Base,
)
from fparser.two.utils import (
    EXTENSIONS,
    InternalError,
)

class Hollerith_Item(Base):  # pylint: disable=invalid-name
    """Hollerith strings take the form `nHx`, where `n` is an integer and
    `x` is a sequence of characters of length `n`.

    Note, the Hollerith format was deprecated in Fortran77 and removed in
    Fortran95. However, Fortran compilers still support it. See, for example
    `<https://gcc.gnu.org/onlinedocs/gcc-4.8.2/gfortran/
    Hollerith-constants-support.html>`_

    """

    subclass_names = []
    use_names = []
    match_pattern = "^[1-9][0-9 ]*[hH]"

    @staticmethod
    def match(string):
        """Implements the matching for a Hollerith string.

        :param str string: The string to check for conformance with a \
                           Hollerith string
        :return: String containing the contents of the Hollerith \
        string.
        :rtype: str

        """
        if "hollerith" not in EXTENSIONS():
            return None
        if not string:
            return None
        # Only strip space to the left as space to the right could be
        # part of the hollerith string.
        strip_string = string.lstrip()
        match = re.search(Hollerith_Item.match_pattern, strip_string)
        if not match:
            return None
        # Current item matches with a hollerith string.
        match_str = match.group(0)
        hol_length_str = match_str[:-1].replace(" ", "")
        hol_length = int(hol_length_str)
        num_chars = len(match_str) + hol_length
        if len(strip_string) < num_chars:
            # The string is too short
            return None
        if len(strip_string) > num_chars:
            # The string is too long
            if strip_string[num_chars:].strip():
                # The extra is not just white space
                return None
        return (strip_string[len(match_str) : num_chars],)

    def tostr(self):
        """
        :return: Parsed representation of a Hollerith String.
        :rtype: str

        :raises InternalError: if the length of the internal items \
        list is not 1.
        :raises InternalError: if the first entry of the internal \
        items list has no content.

        """
        if len(self.items) != 1:
            raise InternalError(
                "Class Hollerith_Item method tostr(): internal items list "
                "should be of length 1 but found '{0}'".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "Class Hollerith_Item method tostr() items entry 0 should be "
                "a valid Hollerith string but it is empty or None"
            )
        return "{0}H{1}".format(len(self.items[0]), self.items[0])
