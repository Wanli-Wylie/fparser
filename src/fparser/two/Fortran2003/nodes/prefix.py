from fparser.two.utils import (
    SequenceBase,
)

from declaration_type_spec import Declaration_Type_Spec
from prefix_spec import Prefix_Spec

class Prefix(SequenceBase):
    """
    Fortran2003 rule R1227::

        prefix is prefix-spec [ prefix-spec ] ...

    C1240 (R1227) A prefix shall contain at most one of each
    prefix-spec. Checked below.

    C1241 (R1227) A prefix shall not specify both ELEMENTAL and
    RECURSIVE. Checked below.

    C1242 (R1227) A prefix shall not specify ELEMENTAL if
    proc-language-binding-spec appears in the function-stmt or
    subroutine-stmt. This constraint can not be checked here, it is
    checked in R1224 and R1232.

    """

    subclass_names = []

    @staticmethod
    def match(string):
        """Match a space separated list of Prefix_Spec objects. Objects may be
        separated by 1 or more spaces.

        :returns: A tuple of size 2 containing the separator and a \
        tuple containing one or more Prefix_Spec objects if there is a \
        match and None if not.

        :rtype: Optional[Tuple[Str, \
                Tuple[:py:class:`fparser.two.Fortran2003.Prefix_Spec`, ...]]]

        """
        start_match_list = []
        end_match_list = []
        decl_spec_list = []
        keyword_list = []
        split = string.split()
        # Match prefix-spec (apart from declaration-type-spec) from
        # the left end of the string. These can be tokenised with a
        # simple split as they are guaranteed to not contain any
        # whitespace (as they are keywords).
        while split and split[0].upper() in Prefix_Spec.keywords:
            start_match_list.append(Prefix_Spec(split[0]))
            keyword_list.append(split[0].upper())
            split = split[1:]
        # Match prefix-spec (apart from declaration-type-spec) from
        # the right end of the string.
        while split and split[-1].upper() in Prefix_Spec.keywords:
            end_match_list.insert(0, Prefix_Spec(split[-1]))
            keyword_list.append(split[-1].upper())
            split = split[:-1]
        # What is remaining must be a declaration-type-spec (or is
        # empty) as only one of each prefix-spec is allowed in a
        # prefix (C1240). This may contain internal white space so
        # join the remaining parts together.
        remaining = " ".join(split)
        if remaining:
            decl_spec_list = [Declaration_Type_Spec(remaining)]
        if len(set(keyword_list)) != len(keyword_list):
            # C1240 A prefix shall contain at most one of each
            # prefix-spec. No need to check declaration-type-spec as
            # that is limited to at most one by design.
            return None
        if "ELEMENTAL" in keyword_list and "RECURSIVE" in keyword_list:
            # C1241 A prefix shall not specify both ELEMENTAL and RECURSIVE.
            return None
        result_list = start_match_list + decl_spec_list + end_match_list
        if result_list:
            return " ", tuple(result_list)
        # A prefix must contain at least one prefix-spec.
        return None
