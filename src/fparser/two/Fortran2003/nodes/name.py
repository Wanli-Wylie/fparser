class Name(StringBase):  # R304
    """
    Fortran 2003 rule R304::

        name is letter [ alphanumeric_character ]...

    """

    # There are no other classes. This is a simple string match.
    subclass_names = []

    @staticmethod
    def match(string):
        """Match the string with the regular expression abs_name in the
        pattern_tools file.

        :param str string: the string to match with the pattern rule.
        :return: a tuple of size 1 containing a string with the \
        matched name if there is a match, or None if there is not.
        :rtype: (str) or None

        """
        return StringBase.match(pattern.abs_name, string.strip())
