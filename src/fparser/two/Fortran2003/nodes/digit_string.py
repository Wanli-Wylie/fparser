class Digit_String(NumberBase):
    """
    ::

        <digit-string> = <digit> [ <digit> ]...

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return NumberBase.match(pattern.abs_digit_string_named, string)
