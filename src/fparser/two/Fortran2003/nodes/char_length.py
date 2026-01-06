class Char_Length(BracketBase):  # R426
    """
    ::

        <char-length> = ( <type-param-value> )
                        | <scalar-int-literal-constant>
    """

    subclass_names = ["Scalar_Int_Literal_Constant"]
    use_names = ["Type_Param_Value"]

    @staticmethod
    def match(string):
        return BracketBase.match("()", Type_Param_Value, string)
