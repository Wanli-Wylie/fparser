class Primary(Base):  # R701
    """
    Fortran 2003 rule R701::

        primary is intrinsic_function_reference
                or constant
                or designator
                or array-constructor
                or structure-constructor
                or function-reference
                or type-param-inquiry
                or type-param-name
                or ( expr )

    `intrinsic_function_reference` is not part of rule R701 but is
    required for fparser to recognise intrinsic functions. This is
    placed before array-constructor in the `subclass_names` list so
    that an intrinsic is not (incorrectly) matched as an array (as
    class `Base` matches rules in list order).

    Note, ( expr ) is implemented in the Parenthesis subclass.

    """

    subclass_names = [
        "Intrinsic_Function_Reference",
        "Constant",
        "Designator",
        "Array_Constructor",
        "Structure_Constructor",
        "Function_Reference",
        "Type_Param_Inquiry",
        "Type_Param_Name",
        "Parenthesis",
    ]
