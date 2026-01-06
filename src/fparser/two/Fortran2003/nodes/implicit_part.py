class Implicit_Part(BlockBase):  # R205
    """
    Fortran2003 Rule R205::

        <implicit-part> = [ <implicit-part-stmt> ]...
                            <implicit-stmt>
    """

    subclass_names = []
    use_names = ["Implicit_Part_Stmt", "Implicit_Stmt"]

    @staticmethod
    def match(reader):
        return BlockBase.match(None, [Implicit_Part_Stmt], None, reader)
