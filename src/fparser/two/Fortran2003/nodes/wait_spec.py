class Wait_Spec(KeywordValueBase):  # R922
    """
    ::

        <wait-spec> = [ UNIT = ] <file-unit-number>
                      | END = <label>
                      | EOR = <label>
                      | ERR = <label>
                      | ID = <scalar-int-expr>
                      | IOMSG = <iomsg-variable>
                      | IOSTAT = <scalar-int-variable>

    """

    subclass_names = []
    use_names = [
        "File_Unit_Number",
        "Label",
        "Scalar_Int_Expr",
        "Iomsg_Variable",
        "Scalar_Int_Variable",
    ]

    @staticmethod
    def match(string):
        for k, v in [
            (["END", "EOR", "ERR"], Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("ID", Scalar_Int_Expr),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)
