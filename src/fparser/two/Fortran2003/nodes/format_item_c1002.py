from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)
from fparser.two.utils import (
    InternalError,
)

from control_edit_desc import Control_Edit_Desc
from data_edit_desc import Data_Edit_Desc
from data_edit_desc_c1002 import Data_Edit_Desc_C1002
from format_item import Format_Item

class Format_Item_C1002(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 constraint C1002::

        format-item-c1002 is kP [,] (F|D)w.d | (E|EN|ES|G)w.d[Ee]
                          or [r]/ [,] format-item
                          or : [,] format-item
                          or format-item [,] / [[,] format-item]
                          or format-item [,] : [[,] format-item]

    C1002 (R1002) The comma used to separate format-items in a
    format-item-list may be omitted

    (1) Between a P edit descriptor and an immediately following F, E,
    EN, ES, D, or G edit descriptor, possibly preceded by a repeat
    specifier,

    (2) Before a slash edit descriptor when the optional repeat
    specification is not present (10.7.2),

    (3) After a slash edit descriptor, or

    (4) Before or after a colon edit descriptor.

    """

    subclass_names = []
    use_names = ["K", "W", "D", "E", "Format_Item", "R"]

    @staticmethod
    def match(string):
        """Implements the matching for the C1002 Format Item constraint. The
        constraints specify certain combinations of format items that
        do not need a comma to separate them. Rather than sorting this
        out when parsing the list, it was decided to treat these
        separately and match them in this class. As a result the
        generated class hierarchy is a little more complicated.

        :param str string: The string to check for conformance with a \
                           C1002 format item constraint.
        :return: `None` if there is no match, otherwise a tuple of \
        size 2 containing a mixture of Control_Edit_Descriptor and \
        Format_Item classes depending on what has been matched.

        :rtype: `NoneType` or ( \
        :py:class:`fparser.two.Control_Edit_Desc`, \
        :py:class:`fparser.two.Format_Item` ) or \
        (:py:class:`fparser.two.Format_Item`, \
        :py:class:`fparser.two.Control_Edit_Desc`) or \
        (:py:class:`fparser.two.Format_Item`, \
        :py:class:`fparser.two.Format_Item`)

        """
        if not string:
            return None
        strip_string = string.strip()
        if len(strip_string) <= 1:
            return None
        if strip_string[0] in ":/":
            # No comma is required after slash edit descriptor (3) or
            # after a colon edit descriptor (4)
            return (
                Control_Edit_Desc(strip_string[0]),
                Format_Item(strip_string[1:].lstrip()),
            )
        if strip_string[-1] in ":/":
            # No comma is required before a slash edit descriptor,
            # when the optional repeat specification is not present
            # (2), or before a colon edit descriptor (4). Note, if an
            # optional repeat specification is present it will be
            # treated as if it is part of the previous item.
            return (
                Format_Item(strip_string[:-1].rstrip()),
                Control_Edit_Desc(strip_string[-1]),
            )
        # We may have a P edit descriptor (which requires a number
        # before the 'P') (1) or a slash edit descriptor with a repeat
        # specifier (3) so look for the repeat specifier.
        found, index = skip_digits(strip_string)
        if found:
            # We found a possible repeat specifier (which may contain
            # white space after the first digit)
            result = strip_string[index].upper()
            if result == "/":
                # We found a possible slash edit descriptor with a
                # repeat specifier (3).
                return (
                    Control_Edit_Desc(strip_string[: index + 1]),
                    Format_Item(strip_string[index + 1 :].lstrip()),
                )
            if result == "P":
                # We found a possible P edit descriptor (1).
                # Rule C1002 only allows a comma to be ommited between
                # a P edit descriptor and a following F, E, EN, ES, D,
                # or G edit descriptor with an optional repeat
                # specifier. In fparser2 this translates to a
                # Format_Item instance containing a Data_Edit_Desc, or
                # Data_Edit_Desc_C1002 instance as its second item
                # with the data edit descriptor instance's first item
                # specifying the type of edit descriptor.
                lhs = Control_Edit_Desc(strip_string[: index + 1])
                rhs = Format_Item(strip_string[index + 1 :].lstrip())
                if not isinstance(rhs, Format_Item):
                    # Matched with a subclass of Format_item or no match.
                    return None
                descriptor_object = rhs.items[1]
                if not isinstance(
                    descriptor_object, (Data_Edit_Desc, Data_Edit_Desc_C1002)
                ):
                    return None
                edit_descriptor = descriptor_object.items[0]
                if edit_descriptor.upper() not in ["F", "E", "EN", "ES", "D", "G"]:
                    return None
                return lhs, rhs

        # Replace any content inside strings etc. so we dont split the
        # line in the wrong place.
        line, repmap = string_replace_map(strip_string)

        # Slash and colon edit descriptors may have no comma's both
        # before and after them (2,3,4) e.g. ('a' / 'b'). To match this
        # situation we split the line with the first potential descriptor found
        # in the string and try to match the lhs and rhs separately
        # (adding the edit descriptor to the RHS).
        for option in "/:":
            if option in line:
                left, right = line.split(option, 1)
                return (
                    Format_Item(repmap(left.rstrip())),
                    Format_Item(option + repmap(right.lstrip())),
                )

    def tostr(self):
        """
        :return: Parsed representation of two format items
        :rtype: str

        :raises InternalError: if the length of the internal items \
        list is not 2.
        :raises InternalError: if the first entry of the internal \
        items list has no content.
        :raises InternalError: if the second entry of the internal \
        items list has no content.

        """
        if len(self.items) != 2:
            raise InternalError(
                "Class Format_Item_C1002 method tostr(): internal items list "
                "should be length 2 but found '{0}'".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "Class Format_Item_C1002 method tostr() items entry 0 should "
                "contain a format items object but it is empty or None"
            )
        if not self.items[1]:
            raise InternalError(
                "Class Format_Item_C1002 method tostr() items entry 1 should "
                "contain a format items object but it is empty or None"
            )
        return "{0}, {1}".format(self.items[0], self.items[1])
