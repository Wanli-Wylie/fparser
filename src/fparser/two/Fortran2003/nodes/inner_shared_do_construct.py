class Inner_Shared_Do_Construct(BlockBase):  # R841
    """
    ::

        <inner-shared-do-construct> = <label-do-stmt>
                                          <do-body>
                                          <do-term-shared-stmt>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Do_Body", "Do_Term_Shared_Stmt"]

    @staticmethod
    def match(reader):
        content = []
        for cls in [Label_Do_Stmt, Do_Body, Do_Term_Shared_Stmt]:
            obj = cls(reader)
            if obj is None:  # todo: restore reader
                return
            content.append(obj)
        return (content,)
