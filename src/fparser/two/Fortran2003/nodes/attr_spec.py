class Attr_Spec(STRINGBase):  # R503
    """
    ::

        <attr-spec> = <access-spec>
                      | ALLOCATABLE
                      | ASYNCHRONOUS
                      | DIMENSION ( <array-spec> )
                      | EXTERNAL
                      | INTENT ( <intent-spec> )
                      | INTRINSIC
                      | <language-binding-spec>
                      | OPTIONAL
                      | PARAMETER
                      | POINTER
                      | PROTECTED
                      | SAVE
                      | TARGET
                      | VALUE
                      | VOLATILE

    """

    subclass_names = [
        "Access_Spec",
        "Language_Binding_Spec",
        "Dimension_Attr_Spec",
        "Intent_Attr_Spec",
    ]
    use_names = []

    @staticmethod
    def match(string):
        return STRINGBase.match(pattern.abs_attr_spec, string)
