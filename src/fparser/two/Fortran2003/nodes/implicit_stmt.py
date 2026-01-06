from implicit_spec import Implicit_Spec_List

class Implicit_Stmt(StmtBase):  # R549
    """
    ::

        <implicit-stmt> = IMPLICIT <implicit-spec-list>
                          | IMPLICIT NONE

    Has attributes::

        items : ({'NONE', Implicit_Spec_List},)

    """

    subclass_names = []
    use_names = ["Implicit_Spec_List"]

    @staticmethod
    def match(string: str):
        """
        Attempts to match the supplied string with an IMPLICIT statement.

        :param string: the string to attempt to match.

        :returns: the Implicit_Spec_List resulting from the match or None.
        :rtype: Union[None, Tuple[str], Tuple[Implicit_Spec_List]]

        """
        if string[:8].upper() != "IMPLICIT":
            return
        line = string[8:].lstrip()
        if len(line) == 4 and line.upper() == "NONE":
            return ("NONE",)
        return (Implicit_Spec_List(line),)

    def tostr(self):
        return "IMPLICIT %s" % (self.items[0])
