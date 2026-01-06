class Intrinsic_Name(STRINGBase):  # No explicit rule
    """Represents the name of a Fortran intrinsic function.

    All generic intrinsic names are specified as keys in the
    `generic_function_names` dictionary, with their values indicating
    the minimum and maximum number of arguments allowed for this
    intrinsic function. A `-1` indicates an unlimited number of
    arguments. The names are split into the categories specified in
    the Fortran2003 specification document.

    All specific intrinsic names (which have a different name to their
    generic counterpart) are specified as keys in the
    `specific_function_names` dictionary, with their values indicating
    which generic function they are associated with.

    """

    numeric_names = {
        "ABS": {"min": 1, "max": 1},
        "AIMAG": {"min": 1, "max": 1},
        "AINT": {"min": 1, "max": 2},
        "ANINT": {"min": 1, "max": 2},
        "CEILING": {"min": 1, "max": 2},
        "CMPLX": {"min": 1, "max": 3},
        "CONJG": {"min": 1, "max": 1},
        "DBLE": {"min": 1, "max": 1},
        "DIM": {"min": 2, "max": 2},
        "DPROD": {"min": 2, "max": 2},
        "FLOOR": {"min": 1, "max": 2},
        "INT": {"min": 1, "max": 2},
        "MAX": {"min": 2, "max": None},
        "MIN": {"min": 2, "max": None},
        "MOD": {"min": 2, "max": 2},
        "MODULO": {"min": 2, "max": 2},
        "NINT": {"min": 1, "max": 2},
        "REAL": {"min": 1, "max": 2},
        "SIGN": {"min": 2, "max": 2},
    }

    mathematical_names = {
        "ACOS": {"min": 1, "max": 1},
        "ASIN": {"min": 1, "max": 1},
        "ATAN": {"min": 1, "max": 1},
        "ATAN2": {"min": 2, "max": 2},
        "COS": {"min": 1, "max": 1},
        "COSH": {"min": 1, "max": 1},
        "EXP": {"min": 1, "max": 1},
        "LOG": {"min": 1, "max": 1},
        "LOG10": {"min": 1, "max": 1},
        "SIN": {"min": 1, "max": 1},
        "SINH": {"min": 1, "max": 1},
        "SQRT": {"min": 1, "max": 1},
        "TAN": {"min": 1, "max": 1},
        "TANH": {"min": 1, "max": 1},
    }

    # Removed max and min from this dictionary as they already appear
    # in numeric_function_names.
    character_names = {
        "ACHAR": {"min": 1, "max": 2},
        "ADJUSTL": {"min": 1, "max": 1},
        "ADJUSTR": {"min": 1, "max": 1},
        "CHAR": {"min": 1, "max": 2},
        "IACHAR": {"min": 1, "max": 2},
        "ICHAR": {"min": 1, "max": 2},
        "INDEX": {"min": 2, "max": 4},
        "LEN_TRIM": {"min": 1, "max": 2},
        "LGE": {"min": 2, "max": 2},
        "LGT": {"min": 2, "max": 2},
        "LLE": {"min": 2, "max": 2},
        "LLT": {"min": 2, "max": 2},
        "REPEAT": {"min": 2, "max": 2},
        "SCAN": {"min": 2, "max": 4},
        "TRIM": {"min": 1, "max": 1},
        "VERIFY": {"min": 2, "max": 4},
    }

    kind_names = {
        "KIND": {"min": 1, "max": 1},
        "SELECTED_CHAR_KIND": {"min": 1, "max": 1},
        "SELECTED_INT_KIND": {"min": 1, "max": 1},
        "SELECTED_REAL_KIND": {"min": 1, "max": 2},
    }

    miscellaneous_type_conversion_names = {
        "LOGICAL": {"min": 1, "max": 2},
        "TRANSFER": {"min": 2, "max": 3},
    }

    numeric_inquiry_names = {
        "DIGITS": {"min": 1, "max": 1},
        "EPSILON": {"min": 1, "max": 1},
        "HUGE": {"min": 1, "max": 1},
        "MAXEXPONENT": {"min": 1, "max": 1},
        "MINEXPONENT": {"min": 1, "max": 1},
        "PRECISION": {"min": 1, "max": 1},
        "RADIX": {"min": 1, "max": 1},
        "RANGE": {"min": 1, "max": 1},
        "TINY": {"min": 1, "max": 1},
    }

    array_inquiry_names = {
        "LBOUND": {"min": 1, "max": 3},
        "SHAPE": {"min": 1, "max": 2},
        "SIZE": {"min": 1, "max": 3},
        "UBOUND": {"min": 1, "max": 3},
    }

    other_inquiry_names = {
        "ALLOCATED": {"min": 1, "max": 1},
        "ASSOCIATED": {"min": 1, "max": 2},
        "BIT_SIZE": {"min": 1, "max": 1},
        "EXTENDS_TYPE_OF": {"min": 2, "max": 2},
        "LEN": {"min": 1, "max": 2},
        "NEW_LINE": {"min": 1, "max": 1},
        "PRESENT": {"min": 1, "max": 1},
        "SAME_TYPE_AS": {"min": 2, "max": 2},
    }

    bit_manipulation_names = {
        "BTEST": {"min": 2, "max": 2},
        "IAND": {"min": 2, "max": 2},
        "IBCLR": {"min": 2, "max": 2},
        "IBITS": {"min": 3, "max": 3},
        "IBSET": {"min": 2, "max": 2},
        "IEOR": {"min": 2, "max": 2},
        "IOR": {"min": 2, "max": 2},
        "ISHFT": {"min": 2, "max": 2},
        "ISHFTC": {"min": 2, "max": 3},
        "MVBITS": {"min": 5, "max": 5},
        "NOT": {"min": 1, "max": 1},
    }

    floating_point_manipulation_names = {
        "EXPONENT": {"min": 1, "max": 1},
        "FRACTION": {"min": 1, "max": 1},
        "NEAREST": {"min": 2, "max": 2},
        "RRSPACING": {"min": 1, "max": 1},
        "SCALE": {"min": 2, "max": 2},
        "SET_EXPONENT": {"min": 2, "max": 2},
        "SPACING": {"min": 1, "max": 1},
    }

    vector_and_matrix_multiply_names = {
        "DOT_PRODUCT": {"min": 2, "max": 2},
        "MATMUL": {"min": 2, "max": 2},
    }

    array_reduction_names = {
        "ALL": {"min": 1, "max": 2},
        "ANY": {"min": 1, "max": 2},
        "COUNT": {"min": 1, "max": 3},
        "MAXVAL": {"min": 1, "max": 3},
        "MINVAL": {"min": 1, "max": 3},
        "PRODUCT": {"min": 1, "max": 3},
        "SUM": {"min": 1, "max": 3},
    }

    array_construction_names = {
        "CSHIFT": {"min": 2, "max": 3},
        "EOSHIFT": {"min": 2, "max": 4},
        "MERGE": {"min": 3, "max": 3},
        "PACK": {"min": 2, "max": 3},
        "RESHAPE": {"min": 2, "max": 4},
        "SPREAD": {"min": 3, "max": 3},
        "TRANSPOSE": {"min": 1, "max": 1},
        "UNPACK": {"min": 3, "max": 3},
    }

    array_location_names = {
        "MAXLOC": {"min": 1, "max": 4},
        "MINLOC": {"min": 1, "max": 4},
    }

    null_names = {"NULL": {"min": 0, "max": 1}}

    allocation_transfer_names = {"MOVE_ALLOC": {"min": 2, "max": 2}}

    random_number_names = {
        "RANDOM_NUMBER": {"min": 1, "max": 1},
        "RANDOM_SEED": {"min": 0, "max": 3},
    }

    system_environment_names = {
        "COMMAND_ARGUMENT_COUNT": {"min": 0, "max": 0},
        "CPU_TIME": {"min": 1, "max": 1},
        "DATE_AND_TIME": {"min": 0, "max": 4},
        "GET_COMMAND": {"min": 0, "max": 3},
        "GET_COMMAND_ARGUMENT": {"min": 1, "max": 4},
        "GET_ENVIRONMENT_VARIABLE": {"min": 1, "max": 5},
        "IS_IOSTAT_END": {"min": 1, "max": 1},
        "IS_IOSTAT_EOR": {"min": 1, "max": 1},
        "SYSTEM_CLOCK": {"min": 0, "max": 3},
    }

    # A map from specific function names to their generic equivalent.
    specific_function_names = {
        "ALOG": "LOG",
        "ALOG10": "LOG10",
        "AMAX0": "MAX",
        "AMAX1": "MAX",
        "AMIN0": "MIN",
        "AMIN1": "MIN",
        "AMOD": "MOD",
        "CABS": "ABS",
        "CCOS": "COS",
        "CEXP": "EXP",
        "CLOG": "LOG",
        "CSIN": "SIN",
        "CSQRT": "SQRT",
        "DABS": "ABS",
        "DACOS": "ACOS",
        "DASIN": "ASIN",
        "DATAN": "ATAN",
        "DATAN2": "ATAN2",
        "DCOS": "COS",
        "DCOSH": "COSH",
        "DDIM": "DIM",
        "DEXP": "EXP",
        "DINT": "AINT",
        "DLOG": "LOG",
        "DLOG10": "LOG10",
        "DMAX1": "MAX",
        "DMIN1": "MIN",
        "DMOD": "MOD",
        "DNINT": "ANINT",
        "DSIGN": "SIGN",
        "DSIN": "SIN",
        "DSINH": "SINH",
        "DSQRT": "SQRT",
        "DTAN": "TAN",
        "DTANH": "TANH",
        "FLOAT": "REAL",
        "IABS": "ABS",
        "IDIM": "DIM",
        "IDINT": "INT",
        "IDNINT": "NINT",
        "IFIX": "INT",
        "ISIGN": "SIGN",
        "MAX0": "MAX",
        "MAX1": "MAX",
        "MIN0": "MIN",
        "MIN1": "MIN",
        "SNGL": "REAL",
    }

    generic_function_names = {}
    generic_function_names.update(numeric_names)
    generic_function_names.update(mathematical_names)
    generic_function_names.update(character_names)
    generic_function_names.update(kind_names)
    generic_function_names.update(miscellaneous_type_conversion_names)
    generic_function_names.update(numeric_inquiry_names)
    generic_function_names.update(array_inquiry_names)
    generic_function_names.update(other_inquiry_names)
    generic_function_names.update(bit_manipulation_names)
    generic_function_names.update(floating_point_manipulation_names)
    generic_function_names.update(vector_and_matrix_multiply_names)
    generic_function_names.update(array_reduction_names)
    generic_function_names.update(array_construction_names)
    generic_function_names.update(array_location_names)
    generic_function_names.update(null_names)
    generic_function_names.update(allocation_transfer_names)
    generic_function_names.update(random_number_names)
    generic_function_names.update(system_environment_names)

    # A list of all function names
    function_names = list(generic_function_names.keys()) + list(
        specific_function_names.keys()
    )

    subclass_names = []

    @staticmethod
    def match(string):
        """Attempt to match the input `string` with the intrinsic function
        names defined in `generic_function_names` or
        `specific_function_names`. If there is a match the resultant
        string will be converted to upper case.

        :param str string: The pattern to be matched.

        :returns: A tuple containing the matched string (converted to \
        upper case) if there is a match or None if there is not.
        :rtype: (str,) or NoneType

        """
        return STRINGBase.match(Intrinsic_Name.function_names, string)
