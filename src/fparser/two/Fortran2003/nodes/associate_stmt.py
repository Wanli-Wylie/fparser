class Associate_Stmt(StmtBase, CALLBase):  # R817
    """
    ::

        <associate-stmt> = [ <associate-construct-name> : ]
            ASSOCIATE ( <association-list> )

    """

    subclass_names = []
    use_names = ["Associate_Construct_Name", "Association_List"]

    @staticmethod
    def match(string):
        return CALLBase.match("ASSOCIATE", Association_List, string)

    def get_start_name(self):
        return self.item.name
