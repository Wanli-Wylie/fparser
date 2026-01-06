from equivalence_set import Equivalence_Set_List

class Equivalence_Stmt(StmtBase, WORDClsBase):  # R554
    """
    ::

        <equivalence-stmt> = EQUIVALENCE <equivalence-set-list>

    """

    subclass_names = []
    use_names = ["Equivalence_Set_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match("EQUIVALENCE", Equivalence_Set_List, string)
