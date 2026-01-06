from derived_type_spec import Derived_Type_Spec

class Declaration_Type_Spec(Base):  # R502
    """
    ::

        <declaration-type-spec> = <intrinsic-type-spec>
                                  | TYPE ( <derived-type-spec> )
                                  | CLASS ( <derived-type-spec> )
                                  | CLASS ( * )

    """

    subclass_names = ["Intrinsic_Type_Spec"]
    use_names = ["Derived_Type_Spec"]

    @staticmethod
    def match(string):
        """Implements the matching of a declaration type specification.

        :param str string: the reader or string to match as a \
        declaration type specification.

        :return: A tuple of size 2 containing a string with the value \
        'TYPE' or 'CLASS' and a 'Derived_Type_Spec' instance if there \
        is a match or None if not.
        :rtype: Optional[Tuple[Str, \
            py:class:`fparser.two.Fortran2003.Derived_Type_Spec`]

        """
        if not string:
            return None
        if string[-1] != ")":
            return None
        start = string[:4].upper()
        if start == "TYPE":
            line = string[4:].lstrip()
            if not line.startswith("("):
                return None
            return "TYPE", Derived_Type_Spec(line[1:-1].strip())
        start = string[:5].upper()
        if start == "CLASS":
            line = string[5:].lstrip()
            if not line.startswith("("):
                return None
            line = line[1:-1].strip()
            if line == "*":
                return "CLASS", "*"
            return "CLASS", Derived_Type_Spec(line)
        return None

    def tostr(self):
        return "%s(%s)" % self.items
