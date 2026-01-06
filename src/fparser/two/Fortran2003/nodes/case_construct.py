class Case_Construct(BlockBase):  # R808
    """
    ::

        <case-construct> = <select-case-stmt>
                               [ <case-stmt>
                                 <block> == [<execution-part-construct>]..
                               ]..
                               <end-select-stmt>

    """

    subclass_names = []
    use_names = [
        "Select_Case_Stmt",
        "Case_Stmt",
        "End_Select_Stmt",
        "Execution_Part_Construct",
    ]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Select_Case_Stmt,
            [Case_Stmt, Execution_Part_Construct, Case_Stmt],
            End_Select_Stmt,
            reader,
            match_names=True,  # C803
            strict_match_names=True,  # C803
            match_name_classes=(Case_Stmt),
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
            if isinstance(item, Case_Stmt):
                tmp.append(item.tofortran(tab=tab, isfix=isfix))
            else:
                tmp.append(item.tofortran(tab=tab + "  ", isfix=isfix))
        tmp.append(end.tofortran(tab=tab, isfix=isfix))
        return "\n".join(tmp)
