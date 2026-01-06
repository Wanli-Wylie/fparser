class Data_Edit_Desc_C1002(Base):
    """This class helps implement the matching for the first part of the
    Fortran 2003 Constraint C1002 which constrains rule R1002. In
    particular it matches with the subset of edit descriptors that can
    follow a P edit descriptor without needing a comma, see below.

    C1002 (applied to R1002) The comma used to separate format-items
    in a format-item-list may be omitted

    (1) Between a P edit descriptor and an immediately following F, E,
    EN, ES, D, or G edit descriptor, possibly preceded by a
    repeat specifier.

    [Remaining constraint clauses ommitted as they are not relevant
    here.]

    ::

        data-edit-desc is F w . d
                       or E w . d [ E e ]
                       or EN w . d [ E e ]
                       or ES w . d [ E e]
                       or G w . d [ E e ]
                       or D w . d

    """

    subclass_names = []
    use_names = ["W", "D", "E"]

    @staticmethod
    def match(string):
        """Check whether the input matches the rule.

        param str string: contains the Fortran that we are trying to \
        match.
        :return: `None` if there is no match, otherwise a `tuple` of \
        size 4, the first entry containing a string with one of ['F', \
        'E', 'EN', 'ES', 'G', 'D'], the second entry containing a W \
        class instance, the third entry containing D class instance \
        and the fourth entry containing either None or an E class \
        instance.
        :rtype: `NoneType`, (`str`, :py:class:`fparser.two.W`, \
        :py:class:`fparser.two.D`, `NoneType`) or, (`str`, \
        :py:class:`fparser.two.W`, :py:class:`fparser.two.D`, \
        :py:class:`fparser.two.E`)

        """
        if not string:
            return None
        strip_string = string.strip()
        if not strip_string:
            return None
        char = strip_string[0].upper()
        if char in ["F", "D"]:
            # match w . d
            my_str = strip_string[1:].lstrip().upper()
            if "." in my_str:
                left, right = my_str.split(".", 1)
                left = left.rstrip()
                right = right.lstrip()
                return char, W(left), D(right), None
            return None
        if char in ["E", "G"]:
            # match w . d [ E e ]
            # Format descriptor could also be 'ES' or 'EN'
            my_str = strip_string[1:].lstrip().upper()
            char2 = my_str[0]
            if char == "E" and char2 in ["S", "N"]:
                my_str = my_str[1:].lstrip()
            else:
                char2 = ""
            if "." not in my_str:
                return None
            left, right = my_str.split(".", 1)
            left = left.rstrip()
            right = right.lstrip()
            # Can optionally specify the number of digits for the
            # exponent
            if right.count("E") >= 1:
                middle, right = right.split("E", 1)
                middle = middle.rstrip()
                right = right.lstrip()
                return char + char2, W(left), D(middle), E(right)
            return char + char2, W(left), D(right), None
        # Invalid char
        return None

    def tostr(self):
        """
        :return: parsed representation of a Data Edit Descriptor \
        conforming to constraint C1002.
        :rtype: str

        :raises InternalError: if the length of the internal items \
        list is not 4.
        :raises InternalError: if the first, second or third entry of \
        the internal items list has no content.
        :raises InternalError: if the value of the first entry is \
        unsupported.
        :raises InternalError: if the value of the first entry is 'F' \
        or 'D' and the fourth entry has content.
        :raises InternalError: if the value of the first entry is 'E', \
        'EN', 'ES' or 'G' and the fourth entry is empty or None.

        """
        if not len(self.items) == 4:
            raise InternalError(
                "Class Data_Edit_Desc_C1002 method tostr() has '{0}' items, "
                "but expecting 4.".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "items[0] in Class Data_Edit_Desc_C1002 method tostr() "
                "should be a descriptor name but is empty or None"
            )
        if not self.items[1]:
            raise InternalError(
                "items[1] in Class Data_Edit_Desc_C1002 method tostr() "
                "should be the w value but is empty or None"
            )
        if not self.items[2]:
            raise InternalError(
                "items[2] in Class Data_Edit_Desc_C1002 method tostr() "
                "should be the m value but is empty or None"
            )
        descriptor_name = self.items[0]
        if descriptor_name in ["F", "D"]:
            if self.items[3]:
                raise InternalError(
                    "items[3] in Class Data_Edit_Desc_C1002 method tostr() "
                    "has an exponent value '{0}' but this is not allowed for "
                    "'F' and 'D' descriptors and should therefore be "
                    "None".format(self.items[3])
                )
            return "{0}{1}.{2}".format(descriptor_name, self.items[1], self.items[2])
        elif descriptor_name in ["E", "EN", "ES", "G"]:
            if self.items[3] is None:
                return "{0}{1}.{2}".format(
                    descriptor_name, self.items[1], self.items[2]
                )
            return "{0}{1}.{2}E{3}".format(
                descriptor_name, self.items[1], self.items[2], self.items[3]
            )
        raise InternalError(
            "Unexpected descriptor name '{0}' in Class Data_Edit_Desc_C1002 "
            "method tostr()".format(descriptor_name)
        )
