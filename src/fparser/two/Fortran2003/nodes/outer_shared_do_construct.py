class Outer_Shared_Do_Construct(BlockBase):  # R839
    """
    ::

        <outer-shared-do-construct> = <label-do-stmt>
                                          <do-body>
                                          <shared-term-do-construct>

    """

    subclass_names = []
    use_names = ["Label_Do_Stmt", "Do_Body", "Shared_Term_Do_Construct"]

    @staticmethod
    def match(reader):
        content = []
        for cls in [Label_Do_Stmt, Do_Body, Shared_Term_Do_Construct]:
            obj = cls(reader)
            if obj is None:  # todo: restore reader
                return
            content.append(obj)
        return (content,)
