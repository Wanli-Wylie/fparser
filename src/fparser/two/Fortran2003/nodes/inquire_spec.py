class Inquire_Spec(KeywordValueBase):  # R930
    """
    Fortran2003 Rule R930::

        <inquire-spec> = [ UNIT = ] <file-unit-number>
                         | FILE = <file-name-expr>
                         | ACCESS = <scalar-default-char-variable>
                         | ACTION = <scalar-default-char-variable>
                         | ASYNCHRONOUS = <scalar-default-char-variable>
                         | BLANK = <scalar-default-char-variable>
                         | DECIMAL = <scalar-default-char-variable>
                         | DELIM = <scalar-default-char-variable>
                         | DIRECT = <scalar-default-char-variable>
                         | ENCODING = <scalar-default-char-variable>
                         | ERR = <label>
                         | EXIST = <scalar-default-logical-variable>
                         | FORM = <scalar-default-char-variable>
                         | FORMATTED = <scalar-default-char-variable>
                         | ID = <scalar-int-expr>
                         | IOMSG = <iomsg-variable>
                         | IOSTAT = <scalar-int-variable>
                         | NAME = <scalar-default-char-variable>
                         | NAMED = <scalar-default-logical-variable>
                         | NEXTREC = <scalar-int-variable>
                         | NUMBER = <scalar-int-variable>
                         | OPENED = <scalar-default-logical-variable>
                         | PAD = <scalar-default-char-variable>
                         | PENDING = <scalar-default-logical-variable>
                         | POS = <scalar-int-variable>
                         | POSITION = <scalar-default-char-variable>
                         | READ = <scalar-default-char-variable>
                         | READWRITE = <scalar-default-char-variable>
                         | RECL = <scalar-int-variable>
                         | ROUND = <scalar-default-char-variable>
                         | SEQUENTIAL = <scalar-default-char-variable>
                         | SIGN = <scalar-default-char-variable>
                         | SIZE = <scalar-int-variable>
                         | STREAM = <scalar-default-char-variable>
                         | UNFORMATTED = <scalar-default-char-variable>
                         | WRITE = <scalar-default-char-variable>

    The `items` attribute for this class contains (str, instance).

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "File_Name_Expr",
        "Scalar_Default_Char_Variable",
        "Scalar_Default_Logical_Variable",
        "Scalar_Int_Variable",
        "Scalar_Int_Expr",
        "Label",
        "Iomsg_Variable",
    ]

    @staticmethod
    def match(string):
        """
        :param str string: The string to check for conformance with an
                           Inquire_Spec
        :return: 2-tuple of name (e.g. "UNIT") and value or None if
                 string is not a valid Inquire_Spec
        :rtype: 2-tuple where first object represents the name and the
                second the value.
        """
        if "=" not in string:
            # The only argument which need not be named is the unit number
            return "UNIT", File_Unit_Number(string)
        # We have a keyword-value pair. Check whether it is valid...
        for keyword, value in [
            (
                [
                    "ACCESS",
                    "ACTION",
                    "ASYNCHRONOUS",
                    "BLANK",
                    "DECIMAL",
                    "DELIM",
                    "DIRECT",
                    "ENCODING",
                    "FORM",
                    "NAME",
                    "PAD",
                    "POSITION",
                    "READ",
                    "READWRITE",
                    "ROUND",
                    "SEQUENTIAL",
                    "SIGN",
                    "STREAM",
                    "UNFORMATTED",
                    "WRITE",
                ],
                Scalar_Default_Char_Variable,
            ),
            ("ERR", Label),
            (["EXIST", "NAMED", "PENDING", "OPENED"], Scalar_Default_Logical_Variable),
            ("ID", Scalar_Int_Expr),
            (
                ["IOSTAT", "NEXTREC", "NUMBER", "POS", "RECL", "SIZE"],
                Scalar_Int_Variable,
            ),
            ("IOMSG", Iomsg_Variable),
            ("FILE", File_Name_Expr),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(keyword, value, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return None


class Inquire_Spec_List(SequenceBase):
    subclass_names = ["Inquire_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Inquire_Spec, string)

    def __iter__(self):
        return iter(self.items)
