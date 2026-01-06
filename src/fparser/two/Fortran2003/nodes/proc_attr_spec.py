class Proc_Attr_Spec(Base):  # R1213
    """
    ::

        <proc-attr-spec> = <access-spec>
                           | <proc-language-binding-spec>
                           | INTENT ( <intent-spec> )
                           | OPTIONAL
                           | POINTER
                           | PROTECTED
                           | SAVE

    Attributes::

        items : ({'INTENT', 'OPTIONAL', 'POINTER', 'PROTECTED', 'SAVE'}, Intent_Spec)

    """

    subclass_names = ["Access_Spec", "Proc_Language_Binding_Spec"]
    use_names = ["Intent_Spec"]

    @staticmethod
    def match(string):
        """
        Matches procedure arguments.

        :param str string: Candidate string.
        :return: Discovered arguments.
        :rtype: tuple, str or None
        """
        if string[:6].upper() == "INTENT":
            line = string[6:].lstrip()
            if not line:
                return
            if line[0] != "(" or line[-1] != ")":
                return
            return "INTENT", Intent_Spec(line[1:-1].strip())
        if len(string) == 8 and string.upper() == "OPTIONAL":
            return "OPTIONAL", None
        if len(string) == 7 and string.upper() == "POINTER":
            return "POINTER", None
        if len(string) == 9 and string.upper() == "PROTECTED":
            return "PROTECTED", None
        if len(string) == 4 and string.upper() == "SAVE":
            return "SAVE", None

    def tostr(self):
        if self.items[1] is None:
            return "%s" % (self.items[0])
        return "%s(%s)" % (self.items)
