from fparser.two import pattern_tools as pattern
from fparser.two.utils import (
    StringBase,
)

class Include_Filename(StringBase):  # pylint: disable=invalid-name
    """Implements the matching of a filename from an include statement."""

    # There are no other classes. This is a simple string match.
    subclass_names = []

    @staticmethod
    def match(string):
        """Match the string with the regular expression file_name in the
        pattern_tools file. The only content that is not accepted is
        an empty string or white space at the start or end of the
        string.

        :param str string: the string to match with the pattern rule.
        :return: a tuple of size 1 containing a string with the \
        matched name if there is a match, or None if there is not.
        :rtype: (str) or NoneType

        """
        return StringBase.match(pattern.file_name, string)
