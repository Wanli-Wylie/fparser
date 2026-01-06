from part_ref import Part_Ref

class Data_Ref(SequenceBase):
    """
    Fortran 2003 Rule R612::

        data-ref is part-ref [ % part-ref ] ...

    If there is only one part-ref then return a 'Part_Ref' object (or
    another object from a matching sub-rule). If there is more than
    one part-ref then return a 'Data_Ref' object containing the
    part-ref's.

    """

    subclass_names = ["Part_Ref"]
    use_names = []

    @staticmethod
    def match(string):
        """Implements the matching for a data-reference. This defines a series
        of dereferences e.g. a%b%c.

        If there is more than one part-ref then return a 'Data_Ref'
        object containing the part-ref's, otherwise return 'None'. A
        single 'part-ref' is purposely not matched here.

        :param str string: Fortran code to check for a match

        :return: `None` if there is no match, or a tuple containing \
                 the matched operator as a string and another tuple \
                 containing the matched subclasses.

        :rtype: NoneType or (str, (obj, obj, ...))

        """
        # Use SequenceBase as normal, then force no match when there is
        # only one entry in the sequence.
        result = SequenceBase.match(r"%", Part_Ref, string)
        entries = result[1]
        if len(entries) > 1:
            # There is more than one part-ref so return a Data_Ref
            # object containing the part-refs.
            return result
        # There is only one part-ref so return None to indicate there
        # is no match and allow the subclass_names Part_Ref class to
        # match instead.
        return None
