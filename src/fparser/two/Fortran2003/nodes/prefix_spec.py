from fparser.two.utils import (
    STRINGBase,
)

class Prefix_Spec(STRINGBase):  # R1228
    """
    ::

        <prefix-spec> = <declaration-type-spec>
                        | ELEMENTAL
                        | IMPURE
                        | MODULE
                        | PURE
                        | RECURSIVE

    """

    subclass_names = ["Declaration_Type_Spec"]
    # issue #221. IMPURE and MODULE are Fortran2008.
    keywords = ["ELEMENTAL", "IMPURE", "MODULE", "PURE", "RECURSIVE"]

    @staticmethod
    def match(string):
        """
        Matches procedure prefixes.

        :param str string: Candidate string.
        :return: Discovered prefix.
        :rtype: str
        """
        return STRINGBase.match(Prefix_Spec.keywords, string)
