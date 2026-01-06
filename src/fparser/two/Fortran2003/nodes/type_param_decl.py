class Type_Param_Decl(BinaryOpBase):  # R436
    """
    ::
        <type-param-decl> = <type-param-name>
            [ = <scalar-int-initialization-expr> ]

    """

    subclass_names = ["Type_Param_Name"]
    use_names = ["Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string):
        if "=" not in string:
            return
        lhs, rhs = string.split("=", 1)
        lhs = lhs.rstrip()
        rhs = rhs.lstrip()
        if not lhs or not rhs:
            return
        return Type_Param_Name(lhs), "=", Scalar_Int_Initialization_Expr(rhs)


class Type_Param_Decl_List(SequenceBase):
    subclass_names = ["Type_Param_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Param_Decl, string)

    def __iter__(self):
        return iter(self.items)
