class Component_Attr_Spec(STRINGBase):  # R441
    """
    ::

        <component-attr-spec> = POINTER
                                | DIMENSION ( <component-array-spec> )
                                | ALLOCATABLE
                                | <access-spec>

    """

    subclass_names = ["Access_Spec", "Dimension_Component_Attr_Spec"]
    use_names = []
    attributes = ["POINTER", "ALLOCATABLE"]

    @classmethod
    def match(cls, string):
        """Implements the matching for component attribute specifications.

        Note that this is implemented as a `classmethod` (not a
        `staticmethod`), using attribute keywords from the list provided
        as a class property. This allows expanding this list for
        Fortran 2008 without having to reimplement the matching.

        :param str string: the string to match as an attribute.

        :return: None if there is no match, otherwise a 1-tuple \
            containing the matched attribute string.
        :rtype: NoneType or (str,)

        """
        return STRINGBase.match(cls.attributes, string)
