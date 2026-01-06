class Flush_Spec(KeywordValueBase):  # R928
    """
    Fortran2003 Rule R928::

        <flush-spec> = [ UNIT = ] <file-unit-number>
                       | IOMSG = <iomsg-variable>
                       | IOSTAT = <scalar-int-variable>
                       | ERR = <label>

    Attributes::

        items : ({'UNIT', 'IOMSG', 'IOSTAT', 'ERR'}, {File_Unit_Number,
                  Iomsg_Variable, Scalar_Int_Variable, Label})

    """

    subclass_names = []
    use_names = ["File_Unit_Number", "Iomsg_Variable", "Scalar_Int_Variable", "Label"]

    @staticmethod
    def match(string):
        for k, v in [
            ("ERR", Label),
            ("IOSTAT", Scalar_Int_Variable),
            ("IOMSG", Iomsg_Variable),
            ("UNIT", File_Unit_Number),
        ]:
            try:
                obj = KeywordValueBase.match(k, v, string, upper_lhs=True)
            except NoMatchError:
                obj = None
            if obj is not None:
                return obj
        return "UNIT", File_Unit_Number(string)
