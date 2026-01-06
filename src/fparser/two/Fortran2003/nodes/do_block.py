class Do_Block(BlockBase):  # pylint: disable=invalid-name
    """
    R832::

        <do-block> = [ <execution-part-construct> ]...

    """

    subclass_names = ["Block"]
    subclass_names = []
    use_names = ["Execution_Part_Construct"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: code block matching the execution part construct within
                 the "DO" block
        :rtype: string
        """
        return BlockBase.match(None, [Execution_Part_Construct], None, string)
