class Forall_Construct(BlockBase):  # R752
    """
    ::

        <forall-construct> = <forall-construct-stmt>
                                 [ <forall-body-construct> ]...
                                 <end-forall-stmt>

    """

    subclass_names = []
    use_names = ["Forall_Construct_Stmt", "Forall_Body_Construct", "End_Forall_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            Forall_Construct_Stmt,
            [Forall_Body_Construct],
            End_Forall_Stmt,
            reader,
            match_names=True,  # C732
            strict_match_names=True,  # C732
        )
