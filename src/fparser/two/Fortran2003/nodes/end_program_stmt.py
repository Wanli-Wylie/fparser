class End_Program_Stmt(EndStmtBase):  # R1103
    """
    <end-program-stmt> = END [ PROGRAM [ <program-name> ] ]
    """

    subclass_names = []
    use_names = ["Program_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("PROGRAM", Program_Name, string)
