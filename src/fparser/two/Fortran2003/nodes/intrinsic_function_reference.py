class Intrinsic_Function_Reference(CallBase):  # No explicit rule
    """
    Represents Fortran intrinsics::

        function-reference is intrinsic-name ( [ actual-arg-spec-list ] )

    """

    subclass_names = []
    use_names = ["Intrinsic_Name", "Actual_Arg_Spec_List"]

    @staticmethod
    def match(string):
        """Match the string as an intrinsic function. Also check that the
        number of arguments provided matches the number expected by
        the intrinsic.

        :param str string: the string to match with the pattern rule.

        :return: a tuple of size 2 containing the name of the intrinsic
            and its arguments if there is a match, or None if there is not.
        :rtype: Tuple[:py:class:`fparser.two.Fortran2003.Intrinsic_Name`,
            :py:class:`fparser.two.Fortran2003.Actual_Arg_Spec_List`] | NoneType

        :raises InternalSyntaxError: If the number of arguments provided does
            not match the number of arguments expected by the intrinsic and
            there are no wildcard imports that could be bringing a routine
            (that overrides it) into scope.

        """
        result = CallBase.match(Intrinsic_Name, Actual_Arg_Spec_List, string)
        if not result:
            return None

        # There is a match so check the number of args provided
        # matches the number of args expected by the intrinsic.
        function_name = str(result[0])
        function_args = result[1]

        # Check that that this name is not being shadowed (i.e. overridden)
        # by a symbol in scope at this point.
        table = SYMBOL_TABLES.current_scope
        try:
            table.lookup(function_name)
            # We found a matching name so refuse to match this intrinsic.
            return None
        except (KeyError, AttributeError):
            # There is either no matching name in the table or we have
            # no current scoping region.
            pass

        nargs = 0 if function_args is None else len(function_args.items)

        if function_name in Intrinsic_Name.specific_function_names.keys():
            # If this is a specific function then use its generic
            # name to test min and max number of arguments.
            test_name = Intrinsic_Name.specific_function_names[function_name]
        else:
            test_name = function_name

        min_nargs = Intrinsic_Name.generic_function_names[test_name]["min"]
        max_nargs = Intrinsic_Name.generic_function_names[test_name]["max"]

        # None indicates an unlimited number of arguments
        if max_nargs is None:
            if nargs < min_nargs:
                if table and not table.all_symbols_resolved:
                    # Wrong number of arguments to be an intrinsic so it must
                    # be a call to a routine being brought into scope from
                    # elsewhere.
                    return None

                raise InternalSyntaxError(
                    "Intrinsic '{0}' expects at least {1} args but found "
                    "{2}.".format(function_name, min_nargs, nargs)
                )
            # The number of arguments is valid. Return here as
            # further tests will fail due to max_args being
            # None.
            return result
        if min_nargs == max_nargs and nargs != min_nargs:
            if table and not table.all_symbols_resolved:
                return None
            raise InternalSyntaxError(
                "Intrinsic '{0}' expects {1} arg(s) but found {2}."
                "".format(function_name, min_nargs, nargs)
            )
        if min_nargs < max_nargs and (nargs < min_nargs or nargs > max_nargs):
            if table and not table.all_symbols_resolved:
                # Wrong number of arguments to be an intrinsic so it must
                # be a call to a routine being brought into scope from
                # elsewhere.
                return None

            raise InternalSyntaxError(
                "Intrinsic '{0}' expects between {1} and {2} args but "
                "found {3}.".format(function_name, min_nargs, max_nargs, nargs)
            )
        return result
