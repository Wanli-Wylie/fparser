class Position_Edit_Desc(Base):  # R1013
    """
    Fortran 2003 rule R1013::

        position-edit-desc is T n
                           or TL n
                           or TR n
                           or n X

    where n is a positive integer.

    If the extensions list includes the string 'x-format' then 'X'
    without a preceeding integer is also matched. This is a common
    extension in Fortran compilers.

    """

    subclass_names = []
    use_names = ["N"]

    @staticmethod
    def match(string):
        """Check whether the input matches the rule.

        param str string: contains the Fortran that we are trying to \
        match.
        :return: `None` if there is no match, otherwise a `tuple` of \
        size 2 either containing a `string` which is one of "T", "TL" \
        or "TR", followed by an `N` class, or containing an `N` class, \
        or `None`, followed by an "X".
        :rtype: `NoneType`, (`str`, \
        :py:class:`fparser.two.Fortran2003.N`), \
        (:py:class:`fparser.two.Fortran2003.N`, `str`) or (`NoneType`, \
        `str`)

        """
        if not string:
            return None
        strip_string_upper = string.strip().upper()
        if not strip_string_upper:
            # empty input string
            return None
        if strip_string_upper[0] == "T":
            if not len(strip_string_upper) > 1:
                # string is not long enough to be valid
                return None
            if strip_string_upper[1] in "LR":
                # We match TL* or TR* where * is stored in variable
                # rest
                start = strip_string_upper[:2]
                rest = strip_string_upper[2:].lstrip()
            else:
                # We match T* where * is stored in variable rest
                start = strip_string_upper[0]
                rest = strip_string_upper[1:].lstrip()
            # Note, if class N does not match it raises an exception
            number_obj = N(rest)
            return start, number_obj
        if strip_string_upper[-1] == "X":
            # We match *X
            if "x-format" in EXTENSIONS() and len(strip_string_upper) == 1:
                # The match just contains 'X' which is not valid
                # fortran 2003 but is an accepted extension
                return None, "X"
            # Note, if class N does not match it raises an
            # exception
            number_obj = N(strip_string_upper[:-1].rstrip())
            return number_obj, "X"
        else:
            return None

    def tostr(self):
        """
        :return: parsed representation of a Position Edit Descriptor
        :rtype: str
        :raises InternalError: if the length of the internal items \
        list is not 2.
        :raises InternalError: if the second entry of the internal \
        items list has no content.

        """
        if not len(self.items) == 2:
            raise InternalError(
                "Class Position_Edit_Desc method tostr() has '{0}' items, "
                "but expecting 2.".format(len(self.items))
            )
        if not self.items[1]:
            raise InternalError(
                "items[1] in Class Position_Edit_Desc method tostr() is "
                "empty or None"
            )
        if self.items[0]:
            return "{0}{1}".format(self.items[0], self.items[1])
        # This output is only required for the "x-format" extension.
        return "{0}".format(self.items[1])
