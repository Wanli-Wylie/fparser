from fparser.two.utils import (
    STRINGBase,
)

class Module_Nature(STRINGBase):  # pylint: disable=invalid-name
    """
    R1110::

        <module-nature> = INTRINSIC
                          | NON_INTRINSIC

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: keyword describing module nature ("INTRINSIC" or
                 "NON_INTRINSIC") or nothing if no match is found
        :rtype: string
        """
        return STRINGBase.match(["INTRINSIC", "NON_INTRINSIC"], string)
