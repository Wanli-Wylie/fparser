class End_Module_Stmt(EndStmtBase):  # R1106
    """
    <end-module-stmt> = END [ MODULE [ <module-name> ] ]
    """

    subclass_names = []
    use_names = ["Module_Name"]

    @staticmethod
    def match(string):
        return EndStmtBase.match("MODULE", Module_Name, string)
