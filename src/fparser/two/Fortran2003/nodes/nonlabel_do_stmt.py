class Nonlabel_Do_Stmt(StmtBase, WORDClsBase):  # pylint: disable=invalid-name
    """
    R829::

        <nonlabel-do-stmt> = [ <do-construct-name> : ] DO [ <loop-control> ]

    """

    subclass_names = []
    use_names = ["Do_Construct_Name", "Loop_Control"]

    @classmethod
    def match(cls, string):
        """
        :param str string: Fortran code to check for a match.
        :return: code line matching the nonlabeled "DO" statement.
        :rtype: str
        """
        return WORDClsBase.match("DO", cls.loop_control_cls(), string)

    @staticmethod
    def loop_control_cls():
        """
        :returns: Fortran2003 Loop_Control class.
        :rtype: :py:class:`fparser.two.Fortran2003.Loop_Control`

        """
        return Loop_Control

    def get_start_name(self):
        """
        :return: optional labeled "DO" statement name
        :rtype: str
        """
        return self.item.name
