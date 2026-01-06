class Type_Param_Attr_Spec(STRINGBase):  # R437
    """
    ::

        <type-param-attr-spec> = KIND
                                 | LEN

    """

    subclass_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(["KIND", "LEN"], string)
