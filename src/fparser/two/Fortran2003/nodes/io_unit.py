class Io_Unit(StringBase):  # R901
    """
    ::

        <io-unit> = <file-unit-number>
                    | *
                    | <internal-file-variable>

    """

    subclass_names = ["File_Unit_Number", "Internal_File_Variable"]

    @staticmethod
    def match(string):
        return StringBase.match("*", string)
