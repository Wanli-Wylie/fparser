class Execution_Part(BlockBase):  # R208
    """Fortran2003 Rule R208::

    <execution-part> = <executable-construct>
                       | [ <execution-part-construct> ]...

    <execution-part> shall not contain <end-function-stmt>,
    <end-program-stmt>, <end-subroutine-stmt>

    """

    subclass_names = []
    use_names = ["Executable_Construct_C201", "Execution_Part_Construct_C201"]

    @staticmethod
    def match(string):
        return BlockBase.match(
            Executable_Construct_C201, [Execution_Part_Construct_C201], None, string
        )
