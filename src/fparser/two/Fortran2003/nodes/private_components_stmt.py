from fparser.two.utils import (
    StringBase,
    STRINGBase,
)

class Private_Components_Stmt(STRINGBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R447::

        <private-components-stmt> = PRIVATE

    Specifies support for private components statement within a derived type.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: keyword  "PRIVATE" or None if no match is found
        :rtype: str or None
        """
        return StringBase.match("PRIVATE", string.upper())
