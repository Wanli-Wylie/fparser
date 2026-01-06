from fparser.two.utils import walk
from .prefix_spec import Prefix_Spec


def c1242_valid(prefix, binding_spec):
    """If prefix and binding-spec exist then check whether they conform to
    constraint C1242 - "A prefix shall not specify ELEMENTAL if
    proc-language-binding-spec appears in the function-stmt or
    subroutine-stmt."

    :param prefix: matching prefix instance if one exists.
    :type: :py:class:`fparser.two.Fortran2003.Prefix` or `NoneType`
    :param binding_spec: matching binding specification instance if \
        one exists.
    :type binding_spec: \
        :py:class:`fparser.two.Fortran2003.Language_Binding_Spec` or
        `NoneType`
    :returns: False if prefix and binding-spec break constraint C1242, \
        otherwise True.
    :rtype: bool

    """
    if binding_spec and prefix:
        # Prefix(es) may or may not be of type ELEMENTAL
        elemental = any(
            "ELEMENTAL" in str(child) for child in walk(prefix.items, Prefix_Spec)
        )
        if elemental:
            # Constraint C1242. A prefix shall not specify ELEMENTAL if
            # proc-language-binding-spec appears in the function-stmt or
            # subroutine-stmt.
            return False
    return True

