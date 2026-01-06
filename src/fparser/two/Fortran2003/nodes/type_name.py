class Type_Name(Name):  # C424
    """
    ::

        <type-name> = <name>
        <type-name> shall not be DOUBLEPRECISION or the name of intrinsic type

    """

    subclass_names = []
    use_names = []

    @staticmethod
    def match(string):
        if pattern.abs_intrinsic_type_name.match(string):
            return
        return Name.match(string)
