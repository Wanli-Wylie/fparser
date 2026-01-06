class Where_Construct(BlockBase):  # R744
    """
    ::

        <where-construct> = <where-construct-stmt>
                                  [ <where-body-construct> ]...
                                [ <masked-elsewhere-stmt>
                                  [ <where-body-construct> ]...
                                ]...
                                [ <elsewhere-stmt>
                                  [ <where-body-construct> ]... ]
                                <end-where-stmt>

    """

    subclass_names = []
    use_names = [
        "Where_Construct_Stmt",
        "Where_Body_Construct",
        "Masked_Elsewhere_Stmt",
        "Elsewhere_Stmt",
        "End_Where_Stmt",
    ]

    @staticmethod
    def match(string):
        return BlockBase.match(
            Where_Construct_Stmt,
            [
                Where_Body_Construct,
                Masked_Elsewhere_Stmt,
                Where_Body_Construct,
                Elsewhere_Stmt,
                Where_Body_Construct,
            ],
            End_Where_Stmt,
            string,
            match_names=True,  # C730
            strict_match_names=True,  # C730
            match_name_classes=(
                Masked_Elsewhere_Stmt,
                Elsewhere_Stmt,
                End_Where_Stmt,
            ),  # C730
            enable_where_construct_hook=True,
        )

    def tofortran(self, tab="", isfix=None):
        """
        Converts this node (and all children) into Fortran.

        :param str tab: white space to prefix to output.
        :param bool isfix: whether or not to generate fixed-format output.

        :returns: Fortran code.
        :rtype: str

        """
        tmp = []
        start = self.content[0]
        end = self.content[-1]
        tmp.append(start.tofortran(tab=tab, isfix=isfix))
        for item in self.content[1:-1]:
            if isinstance(item, (Masked_Elsewhere_Stmt, Elsewhere_Stmt)):
                tmp.append(item.tofortran(tab=tab, isfix=isfix))
            else:
                tmp.append(item.tofortran(tab=tab + "  ", isfix=isfix))
        tmp.append(end.tofortran(tab=tab, isfix=isfix))
        return "\n".join(tmp)
