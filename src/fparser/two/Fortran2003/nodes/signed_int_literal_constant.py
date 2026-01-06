class Signed_Int_Literal_Constant(NumberBase):  # R405
    """
    ::
        <signed-int-literal-constant> = [ <sign> ] <int-literal-constant>

    """

    # never used because sign is included in pattern
    subclass_names = ["Int_Literal_Constant"]

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_signed_int_literal_constant_named, string)
