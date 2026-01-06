class Format(StringBase):  # R914
    """
    ::

        <format> = <default-char-expr>
                   | <label>
                   | *

    """

    subclass_names = ["Label", "Default_Char_Expr"]

    @staticmethod
    def match(string):
        return StringBase.match("*", string)
