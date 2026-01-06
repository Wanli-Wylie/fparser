class Named_Constant_Def(KeywordValueBase):  # R539
    """
    ::

        <named-constant-def> = <named-constant> = <initialization-expr>

    """

    subclass_names = []
    use_names = ["Named_Constant", "Initialization_Expr"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Named_Constant, Initialization_Expr, string)
