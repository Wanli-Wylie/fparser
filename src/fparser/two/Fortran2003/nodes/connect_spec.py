from default_char_expr import Scalar_Default_Char_Expr
from file_name_expr import File_Name_Expr
from file_unit_number import File_Unit_Number
from int_expr import Scalar_Int_Expr
from int_variable import Scalar_Int_Variable
from iomsg_variable import Iomsg_Variable
from label import Label

class Connect_Spec(KeywordValueBase):
    """
    R905 is:

    connect-spec is [ UNIT = ] file-unit-number
                 or ACCESS = scalar-default-char-expr
                 or ACTION = scalar-default-char-expr
                 or ASYNCHRONOUS = scalar-default-char-expr
                 or BLANK = scalar-default-char-expr
                 [ or CONVERT = scalar-default-char-expr ]
                 or DECIMAL = scalar-default-char-expr
                 or DELIM = scalar-default-char-expr
                 or ENCODING = scalar-default-char-expr
                 or ERR = label
                 or FILE = file-name-expr
                 or FORM = scalar-default-char-expr
                 or IOMSG = iomsg-variable
                 or IOSTAT = scalar-int-variable
                 or PAD = scalar-default-char-expr
                 or POSITION = scalar-default-char-expr
                 or RECL = scalar-int-expr
                 or ROUND = scalar-default-char-expr
                 or SIGN = scalar-default-char-expr
                 or STATUS = scalar-default-char-expr

    Note that CONVERT is not a part of the Fortran standard but is supported
    by several major compilers (Gnu, Intel, Cray etc.) and thus is matched
    by fparser if the utils.EXTENSIONS() list includes the string 'open-convert'.

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "Scalar_Default_Char_Expr",
        "Label",
        "File_Name_Expr",
        "Iomsg_Variable",
        "Scalar_Int_Expr",
        "Scalar_Int_Variable",
    ]

    @classmethod
    def _keyword_value_list(cls):
        """
        Defines the valid keywords and corresponding classes to match against.
        This has to be a method rather than a class property as those classes
        are generated after this class has been created.

        :returns: list of keyword, class pairs to match against.
        :rtype: list[tuple[str, type]]

        """
        result = [
            ("ACCESS", Scalar_Default_Char_Expr),
            ("ACTION", Scalar_Default_Char_Expr),
            ("ASYNCHRONOUS", Scalar_Default_Char_Expr),
            ("BLANK", Scalar_Default_Char_Expr),
            ("DECIMAL", Scalar_Default_Char_Expr),
            ("DELIM", Scalar_Default_Char_Expr),
            ("ENCODING", Scalar_Default_Char_Expr),
            ("FORM", Scalar_Default_Char_Expr),
            ("PAD", Scalar_Default_Char_Expr),
            ("POSITION", Scalar_Default_Char_Expr),
            ("ROUND", Scalar_Default_Char_Expr),
            ("SIGN", Scalar_Default_Char_Expr),
            ("STATUS", Scalar_Default_Char_Expr),
            ("ERR", Label),
            ("FILE", File_Name_Expr),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("RECL", Scalar_Int_Expr),
            ("UNIT", File_Unit_Number),
        ]
        if "open-convert" in EXTENSIONS():
            # The CONVERT keyword is a non-standard extension supported by
            # many compilers.
            result.append(("CONVERT", Scalar_Default_Char_Expr))
        return result

    @classmethod
    def match(cls, string):
        """Implements the matching for connect-spec.

        Note that this is implemented as a `classmethod` (not a
        `staticmethod`), using attribute keywords from the list provided
        as a class method. This allows expanding this list for
        Fortran 2008 without having to reimplement the matching.

        :param str string: Fortran code to check for a match
        :return: 2-tuple containing the keyword and value or None if the
                 supplied string is not a match
        :rtype: 2-tuple containing keyword (e.g. "UNIT") and associated value

        """
        if "=" not in string:
            # The only argument which need not be named is the unit number
            return "UNIT", File_Unit_Number(string)
        # We have a keyword-value pair. Check whether it is valid...
        for keyword, value in cls._keyword_value_list():
            try:
                obj = KeywordValueBase.match(keyword, value, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None


class Connect_Spec_List(SequenceBase):
    subclass_names = ["Connect_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Connect_Spec, string)

    def __iter__(self):
        return iter(self.items)
