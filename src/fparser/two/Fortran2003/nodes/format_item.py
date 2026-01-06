class Format_Item(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R1003::

        format-item is [ r ] data-edit-desc
                    or control-edit-desc
                    or char-string-edit-desc
                    or [ r ] ( format-item-list )
                    or format-item-c1002
                    or hollerith-item

    """

    subclass_names = [
        "Hollerith_Item",
        "Control_Edit_Desc",
        "Char_String_Edit_Desc",
        "Format_Item_C1002",
    ]
    use_names = ["R", "Format_Item_List", "Data_Edit_Desc"]

    @staticmethod
    def match(string):
        """Implements the matching of a Format Item. This method matches '[ r
        ] data-edit-desc' and '[ r ] ( format-item-list )'. The
        remaining options are matched via subclasses specified in the
        subclass_names variable.

        :param str string: A string or the Fortran reader containing the \
                    line of code that we are trying to match.
        :return: `None` if there is no match or a `tuple` of size 2 \
        containing an instance of the R class followed by an \
        instance of either the Format_Item_List or the Data_Edit_Desc \
        class.
        :rtype: `None` or ( :py:class:`fparser.two.Fortran2003.R`, \
        :py:class:`fparser.two.Fortran2003.Format_Item_List` or \
        :py:class:`fparser.two.Fortran2003.Data_Edit_Desc`)

        """
        if not string:
            return None
        strip_string = string.strip()
        if not strip_string:
            return None
        index = 0
        # Look for an optional repeat specifier (the 'r' in this rule)
        found, index = skip_digits(strip_string)
        rpart = None
        my_string = strip_string
        if found:
            # We found a repeat specifier (with content after it) so
            # create an R class using the value
            rpart = R(strip_string[:index])
            my_string = strip_string[index:].lstrip()
        # We deal with format-item-list and data-edit-desc in this
        # match method. Other matches are performed by the subclasses.
        if my_string[0] == "(" and my_string[-1] == ")":
            # This could be a format-item-list
            rest = Format_Item_List(my_string[1:-1].lstrip())
        else:
            # This is not a format-item-list so see if it is a
            # data-edit-descriptor
            rest = Data_Edit_Desc(my_string)
        return rpart, rest

    def tostr(self):
        """
        :return: Parsed representation of a Format Item.
        :rtype: str

        :raises InternalError: if the length of the internal items \
        list is not 2.
        :raises InternalError: if the first entry of the internal \
        items list has no content.

        """
        if len(self.items) != 2:
            raise InternalError(
                "Class Format_Item method tostr(): internal items list "
                "should be of length 2 but found '{0}'".format(len(self.items))
            )
        if not self.items[1]:
            raise InternalError(
                "Class Format_Item method tostr(): items list second entry "
                "should be a valid descriptor but it is empty or None"
            )
        rpart = self.items[0]
        rest = self.items[1]

        rpart_str = rpart if rpart else ""
        if isinstance(rest, (Data_Edit_Desc, Data_Edit_Desc_C1002)):
            return "{0}{1}".format(rpart_str, rest)
        return "{0}({1})".format(rpart_str, rest)
