class Binding_Attr(STRINGBase):  # pylint: disable=invalid-name
    """
    Fortran2003 Rule R453::

        <binding-attr> = PASS [ ( <arg-name> ) ]
                         | NOPASS
                         | NON_OVERRIDABLE
                         | DEFERRED
                         | <access-spec>

    Specifies syntax of allowed binding attributes for a
    specific type-bound procedure binding.

    """

    subclass_names = ["Access_Spec", "Binding_PASS_Arg_Name"]

    @staticmethod
    def match(string):
        """
        :return: keywords for allowed binding attributes or
                 nothing if no match is found
        :rtype: str
        """
        return STRINGBase.match(
            ["PASS", "NOPASS", "NON_OVERRIDABLE", "DEFERRED"], string
        )
