from else_if_stmt import Else_If_Stmt
from else_stmt import Else_Stmt
from end_if_stmt import End_If_Stmt
from execution_part_construct import Execution_Part_Construct
from if_then_stmt import If_Then_Stmt

class If_Construct(BlockBase):  # R802
    """
    ::

        <if-construct> = <if-then-stmt>
                               <block>
                             [ <else-if-stmt>
                               <block>
                             ]...
                             [ <else-stmt>
                               <block>
                             ]
                             <end-if-stmt>

    """

    subclass_names = []
    use_names = [
        "If_Then_Stmt",
        "Execution_Part_Construct",
        "Else_If_Stmt",
        "Else_Stmt",
        "End_If_Stmt",
    ]

    @staticmethod
    def match(string):
        return BlockBase.match(
            If_Then_Stmt,
            [
                Execution_Part_Construct,
                Else_If_Stmt,
                Execution_Part_Construct,
                Else_Stmt,
                Execution_Part_Construct,
            ],
            End_If_Stmt,
            string,
            match_names=True,  # C801
            strict_match_names=True,  # C801
            match_name_classes=(Else_If_Stmt, Else_Stmt, End_If_Stmt),
            enable_if_construct_hook=True,
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
            if isinstance(item, (Else_If_Stmt, Else_Stmt)):
                tmp.append(item.tofortran(tab=tab, isfix=isfix))
            else:
                tmp.append(item.tofortran(tab=tab + "  ", isfix=isfix))
        tmp.append(end.tofortran(tab=tab, isfix=isfix))
        return "\n".join(tmp)
