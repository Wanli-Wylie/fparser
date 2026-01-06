class Real_Literal_Constant(NumberBase):  # R417
    """ """

    subclass_names = []

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_real_literal_constant_named, string)
