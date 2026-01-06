from fparser.two.utils import (
    BracketBase,
)

from format_item import Format_Item_List

class Format_Specification(BracketBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R1002::

        format-specification = ( [ format-item-list ] )

    C1002 is implemented in a separate class Format_Item_C1002

    C1002 (R1002) The comma used to separate format-items in a
    format-item-list may be omitted

    (1) Between a P edit descriptor and an immediately following F, E,
    EN, ES, D, or G edit descriptor, possibly preceded by a repeat
    specifier,

    (2) Before a slash edit descriptor when the optional repeat
    specification is not present,

    (3) After a slash edit descriptor, or

    (4) Before or after a colon edit descriptor.

    """

    subclass_names = []
    use_names = ["Format_Item_List"]

    @staticmethod
    def match(string):
        """Implements the matching for a format specification.

        :param str string: The string to check for conformance with a \
                           format specification.
        :return: `None` if there is no match, otherwise a tuple of \
        size three, the first entry being a string containing a left \
        bracket and the third being a string containing a right \
        bracket. The second entry is either a Format_Item or a \
        Format_Item_List.
        :rtype: `NoneType` or ( `str`, \
        :py:class:`fparser.two.Fortran2003.Format_Item` or \
        :py:class:`fparser.two.Fortran2003.Format_Item_List`, `str` )

        """
        return BracketBase.match("()", Format_Item_List, string, require_cls=False)
