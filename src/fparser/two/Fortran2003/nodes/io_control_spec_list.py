class Io_Control_Spec_List(SequenceBase):
    """
    Rule 913 - Control information list::

        io-control-spec-list is a list of io-control-spec items.

    Subject to the following constraints::

        C909 No specifier shall appear more than once in a given
             io-control-spec-list.
        C910 An io-unit shall be specified; if the optional characters UNIT= are
             omitted, the io-unit shall be the first item in the
             io-control-spec-list.
        C911 A DELIM= or SIGN= specifier shall not appear in a read-stmt.
        C912 A BLANK=, PAD=, END=, EOR=, or SIZE=specifier shall not appear in a
             write-stmt.
        C913 The label in the ERR=, EOR=, or END= specifier shall be the statement
             label of a branch target statement that appears in the same scoping
             unit as the data transfer statement.
        C914 A namelist-group-name shall be the name of a namelist group.
        C915 A namelist-group-name shall not appear if an input-item-list or an
             output-item-list appears in the data transfer statement.
        C916 An io-control-spec-list shall not contain both a format and a
             namelist-group-name.
        C917 If format appears without a preceding FMT=, it shall be the second
             item in the iocontrol-spec-list and the first item shall be io-unit.
        C918 If namelist-group-name appears without a preceding NML=, it shall be
             the second item in the io-control-spec-list and the first item shall
             be io-unit.
        C919 If io-unit is not a file-unit-number, the io-control-spec-list shall
             not contain a REC= specifier or a POS= specifier.
        C920 If the REC= specifier appears, an END= specifier shall not appear, a
             namelist-groupname shall not appear, and the format, if any, shall not
             be an asterisk.
        C921 An ADVANCE= specifier may appear only in a formatted sequential or
             stream input/output statement with explicit format specification
             (10.1) whose control information list does not contain an
             internal-file-variable as the io-unit.
        C922 If an EOR= specifier appears, an ADVANCE= specifier also shall appear.
        C923 If a SIZE= specifier appears, an ADVANCE= specifier also shall appear.
        C924 The scalar-char-initialization-expr in an ASYNCHRONOUS= specifier
             shall be of type default character and shall have the value YES or NO.
        C925 An ASYNCHRONOUS= specifier with a value YES shall not appear unless
             io-unit is a file-unit-number.
        C926 If an ID= specifier appears, an ASYNCHRONOUS= specifier with the value
             YES shall also appear.
        C927 If a POS= specifier appears, the io-control-spec-list shall not
             contain a REC= specifier.
        C928 If a DECIMAL=, BLANK=, PAD=, SIGN=, or ROUND= specifier appears, a
             format or namelist-group-name shall also appear.
        C929 If a DELIM= specifier appears, either format shall be an asterisk or
             namelist-group-name shall appear.

    TODO #267. Of these constraints, only C910 & C916-918 are currently
    enforced.

    """

    subclass_names = []
    use_names = ["Io_Control_Spec", "Namelist_Group_Name", "Format"]

    @staticmethod
    def match(string):
        """
        Attempts to match the supplied string with a list of Io_Control_Spec
        items. We have to override the base implementation because the first
        two items in the list have specific meanings if they are not explictly
        named: the first must be the unit number and the second may be either
        a format specifier *or* a namelist-group-name.

        :param str string: the string that is checked for a match.

        :returns: a tuple of Io_Control_Spec objects if the match is \
                  successful, None otherwise.
        :rtype: tuple of :py:class:`fparser.two.Fortran2003.Io_Control_Spec` \
                objects or NoneType

        """
        line, repmap = string_replace_map(string)
        splitted = line.split(",")
        lst = []

        # Examine the first entry in the list. If it is not named then it must
        # be a unit number (C910).
        have_unit = False
        have_unnamed_nml_or_fmt = False
        spec = splitted.pop(0).strip()
        spec = repmap(spec)

        try:
            try:
                Io_Unit(spec)
                # We matched an unamed unit number. We now need to construct an
                # Io_Control_Spec for it. In order to do so we have to
                # temporarily name it so that Io_Control_Spec matches it.
                io_spec = Io_Control_Spec("unit=" + spec)
                # Remove the name from the new object
                io_spec.items = (None, io_spec.items[1])
                lst.append(io_spec)
                # Record that we have found a unit number for the purpose of
                # performing validation checks.
                have_unit = True

                if not splitted:
                    # The list only has one entry and it is an IO unit
                    return ",", tuple(lst)

                # Since the unit-number was not named, the following item may
                # also not be named if it is a format specifier or namelist
                # group name.
                spec = splitted.pop(0).strip()
                spec = repmap(spec)
                for cls, name in [(Namelist_Group_Name, "nml"), (Format, "fmt")]:
                    try:
                        if cls(spec):
                            # We have a match on an un-named entry. We
                            # temporarily add the name so that Io_Control_Spec
                            # matches the correct one.
                            io_spec = Io_Control_Spec(name + "=" + spec)
                            # Remove the name from the new object
                            io_spec.items = (None, io_spec.items[1])
                            lst.append(io_spec)
                            have_unnamed_nml_or_fmt = True
                            break
                    except NoMatchError:
                        pass
                else:
                    raise NoMatchError("Not an un-named nml-group-name or fmt")

            except NoMatchError:
                # If we get here we failed to match an un-named spec so from
                # here on, they must all be named.
                lst.append(Io_Control_Spec(spec))

            # Deal with the remainder of the list entries. These must all be
            # named.
            for spec in splitted:
                mapped_spec = repmap(spec.strip())
                lst.append(Io_Control_Spec(mapped_spec))

        except NoMatchError:
            return None

        # At this point we need to check the list and apply constraints.
        # TODO #267 enforce remaining constraints.
        have_nml = False
        have_fmt = False
        for spec in lst:
            if spec.children[0] == "UNIT":
                have_unit = True
            elif spec.children[0] == "NML":
                have_nml = True
            elif spec.children[0] == "FMT":
                have_fmt = True
        # C910: An io-unit shall be specified
        if not have_unit:
            return None
        # C916: an io-control-spec-list shall not contain both a format
        # and a namelist-group-name
        if have_nml and have_fmt:
            return None
        if have_unnamed_nml_or_fmt and (have_nml or have_fmt):
            return None

        return ",", tuple(lst)
