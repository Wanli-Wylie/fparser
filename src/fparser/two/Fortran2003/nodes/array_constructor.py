class Array_Constructor(BracketBase):  # R465
    """
    ::

        <array-constructor> = (/ <ac-spec> /)
                              | <left-square-bracket> <ac-spec>
                                <right-square-bracket>

    """

    subclass_names = []
    use_names = ["Ac_Spec"]

    @staticmethod
    def match(string):
        try:
            obj = BracketBase.match("(//)", Ac_Spec, string)
        except NoMatchError:
            obj = None
        if obj is None:
            obj = BracketBase.match("[]", Ac_Spec, string)
        return obj
