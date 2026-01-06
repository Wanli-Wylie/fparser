class Int_Literal_Constant(NumberBase):  # R406
    """
    ::
        <int-literal-constant> = <digit-string> [ _ <kind-param> ]

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_int_literal_constant_named, string)
