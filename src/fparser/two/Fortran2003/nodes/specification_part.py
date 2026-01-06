class Specification_Part(BlockBase):  # R204
    """
    Fortran2003 Rule R204::

        <specification-part> = [ <use-stmt> ]...
                                 [ <import-stmt> ]...
                                 [ <implicit-part> ]
                                 [ <declaration-construct> ]...
    """

    subclass_names = []
    use_names = ["Use_Stmt", "Import_Stmt", "Implicit_Part", "Declaration_Construct"]

    @staticmethod
    def match(reader):
        return BlockBase.match(
            None,
            [Use_Stmt, Import_Stmt, Implicit_Part, Declaration_Construct],
            None,
            reader,
        )
