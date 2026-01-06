class Close_Spec(KeywordValueBase):  # R909
    """
    ::

        <close-spec> = [ UNIT = ] <file-unit-number>
                       | IOSTAT = <scalar-int-variable>
                       | IOMSG = <iomsg-variable>
                       | ERR = <label>
                       | STATUS = <scalar-default-char-expr>

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "Scalar_Default_Char_Expr",
        "Label",
        "Iomsg_Variable",
        "Scalar_Int_Variable",
    ]

    @staticmethod
    def match(string):
        for k, v in [
            ("ERR", Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("STATUS", Scalar_Default_Char_Expr),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)
