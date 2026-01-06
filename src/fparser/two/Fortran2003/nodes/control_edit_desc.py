from k import K
from r import R

class Control_Edit_Desc(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R1011::

        control-edit-desc is position-edit-desc
                          or [ r ] /
                          or :
                          or sign-edit-desc
                          or k P
                          or blank-interp-edit-desc
                          or round-edit-desc
                          or decimal-edit-desc
                          or $

    '$' is used to suppress the carriage return on output.  Note that
    this is an extension to the Fortran standard.

    """

    subclass_names = [
        "Position_Edit_Desc",
        "Sign_Edit_Desc",
        "Blank_Interp_Edit_Desc",
        "Round_Edit_Desc",
        "Decimal_Edit_Desc",
    ]
    use_names = ["R", "K"]

    @staticmethod
    def match(string):
        """Check whether the input matches the rule.

        param str string: contains the Fortran that we are trying to \
        match.
        :return: `None` if there is no match, otherwise a `tuple` of \
        size 2 containing, None and a string with one of '/', ':', or \
        '$', an R class and a string containing '/' or a K class and a \
        string containing 'P'.
        :rtype: `NoneType`, (`NoneType`, `str`), \
        (:py:class:`fparser.two.Fortran2003.R`, `str`), or \
        (:py:class:`fparser.two.Fortran2003.K`, `str`)

        """
        if not string:
            return None
        strip_string = string.strip()
        if not strip_string:
            return None
        if len(strip_string) == 1 and strip_string in "/:$":
            if strip_string == "$" and "dollar-descriptor" not in EXTENSIONS():
                return None
            return None, strip_string
        if strip_string[-1] == "/":
            return R(strip_string[:-1].rstrip()), "/"
        if strip_string[-1].upper() == "P":
            return K(strip_string[:-1].rstrip()), "P"
        return None

    def tostr(self):
        """
        :return: parsed representation of a Control Edit Descriptor
        :rtype: str
        :raises InternalError: if the length of the internal items \
        list is not 2.
        :raises InternalError: if the second entry of the internal \
        items list has no content.

        """
        if len(self.items) != 2:
            raise InternalError(
                "Class Control_Edit_Desc method tostr() has '{0}' items, "
                "but expecting 2.".format(len(self.items))
            )
        if not self.items[1]:
            raise InternalError(
                "items[1] in Class Control_Edit_Desc method tostr() should "
                "be an edit descriptor name but is empty or None"
            )
        if self.items[0] is not None:
            return "{0}{1}".format(self.items[0], self.items[1])
        return "{0}".format(self.items[1])
