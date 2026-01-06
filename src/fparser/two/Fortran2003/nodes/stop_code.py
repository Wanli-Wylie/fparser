from level_3_expr import Level_3_Expr

class Stop_Code(StringBase):  # R850
    """
    ::

        <stop-code> = <scalar-char-constant>
                      | <digit> [ <digit> [ <digit> [ <digit> [ <digit> ] ] ] ]
        Extension:
                      | Level_3_Expr
    """

    subclass_names = ["Scalar_Char_Constant"]

    @staticmethod
    def match(string):
        result = StringBase.match(pattern.abs_label, string)
        if result or not "extended-stop-args" in EXTENSIONS():
            return result
        # This will allow statements like `stop -1` and `stop str1//str2`
        return Level_3_Expr(string)
