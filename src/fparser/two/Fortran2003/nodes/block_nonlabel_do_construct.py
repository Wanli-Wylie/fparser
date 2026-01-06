class Block_Nonlabel_Do_Construct(BlockBase):  # pylint: disable=invalid-name
    """
    R826_2::

       <block-nonlabel-do-construct> = <nonlabel-do-stmt>
                                        [ <execution-part-construct> ]...
                                        <end-do-stmt>

    """

    subclass_names = []
    use_names = ["Nonlabel_Do_Stmt", "Execution_Part_Construct", "End_Do_Stmt"]

    @classmethod
    def match(cls, reader):
        """
        :param reader: instance of `FortranReaderBase` class
        :type reader: :py:class:`FortranReaderBase`
        :return: code block matching the nonlabeled "DO" construct
        :rtype: string
        """
        return BlockBase.match(
            cls.nonlabel_do_stmt_cls(),
            [Execution_Part_Construct],
            End_Do_Stmt,
            reader,
            match_names=True,  # C821
            strict_match_names=True,  # C821
        )

    @staticmethod
    def nonlabel_do_stmt_cls():
        """
        :returns: Fortran2003 Nonlabel_Do_Stmt class.
        :rtype: :py:class:`fparser.two.Fortran2003.Nonlabel_Do_Stmt`

        """
        return Nonlabel_Do_Stmt
