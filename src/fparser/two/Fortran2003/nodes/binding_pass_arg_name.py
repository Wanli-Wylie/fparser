class Binding_PASS_Arg_Name(CALLBase):
    # pylint: disable=invalid-name
    """
    Fortran 2003 helper rule (for R453)::

        <binding-PASS-arg-name> = PASS ( <arg-name> )

    Specifies the syntax of passed-object dummy argument for a
    specific type-bound procedure.

    """
    subclass_names = []
    use_names = ["Arg_Name"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: keyword  "PASS" with the name of a passed-object
                 dummy argument or nothing if no match is found
        :rtype: str
        """
        return CALLBase.match("PASS", Arg_Name, string)
