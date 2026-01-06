from generic_spec import Generic_Spec
from module_nature import Module_Nature
from name import Module_Name
from name import Name
from only import Only_List
from rename import Rename
from rename import Rename_List

class Use_Stmt(StmtBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R1109::

        use-stmt is USE [ [ , module-nature ] :: ] module-name [ , rename-list ]
                 or USE [ [ , module-nature ] :: ] module-name ,
                     ONLY : [ only-list ]

    """

    subclass_names = []
    use_names = ["Module_Nature", "Module_Name", "Rename_List", "Only_List"]

    @staticmethod
    def match(string):
        """
        Wrapper for the match method that captures any successfully-matched
        use statements in the symbol table associated with the current scope
        (if there is one).

        TODO #379 - currently operator imports/renaming are not captured in
                    the symbol table.

        :param str string: Fortran code to check for a match.

        :return: 5-tuple containing strings and instances of the classes
                 describing a module (optional module nature, optional
                 double colon delimiter, mandatory module name, optional
                 "ONLY" specification and optional "Rename" or "Only" list)
                 or None if the match fails.
        :rtype: 5-tuple of objects (module name and 4 optional) or NoneType

        :raises InternalError: if an Only_List is found to contain anything \
                               other than Name or Rename objects.

        """
        result = Use_Stmt._match(string)
        if result:
            table = SYMBOL_TABLES.current_scope
            if table:
                only_list = None
                rename_list = None
                if "only" in result[3].lower():
                    only_list = []
                if isinstance(result[4], Only_List):
                    # An Only_List can contain either Name or Rename entries.
                    for child in result[4].children:
                        if isinstance(child, Name):
                            only_list.append((child.string, None))
                        elif isinstance(child, Rename):
                            if not child.children[0]:
                                # This is a Rename of a symbol rather than an operator
                                # (which would have child.children[0] == 'OPERATOR'.
                                # TODO #379 - support operators.
                                only_list.append(
                                    (child.children[1].string, child.children[2].string)
                                )
                        elif isinstance(child, Generic_Spec):
                            # For now we ignore anything other than symbol names
                            # and this includes operators (TODO #379).
                            pass
                        else:
                            raise InternalError(
                                f"An Only_List can contain only Name, Rename or "
                                f"Generic_Spec entries but found "
                                f"'{type(child).__name__}' when matching '{string}'"
                            )
                elif isinstance(result[4], Rename_List):
                    # Tuples of <local-name>, <use-name>
                    rename_list = []
                    for rename in walk(result[4], Rename):
                        # For now we exclude any operators in the Rename_List
                        # (these have rename.children[0] == 'OPERATOR').
                        # TODO #379.
                        if rename.children[0] is None:
                            rename_list.append(
                                (rename.children[1].string, rename.children[2].string)
                            )

                table.add_use_symbols(str(result[2]), only_list, rename_list)

        return result

    @staticmethod
    def _match(string):
        """
        :param str string: Fortran code to check for a match.

        :return: 5-tuple containing strings and instances of the classes
                 describing a module (optional module nature, optional
                 double colon delimiter, mandatory module name, optional
                 "ONLY" specification and optional "Rename" or "Only" list).
        :rtype: 5-tuple of objects (module name and 4 optional)

        """
        line = string.strip()
        # Incorrect 'USE' statement or line too short
        if line[:3].upper() != "USE":
            return None
        line = line[3:]
        # Empty string after 'USE'
        if not line:
            return None
        # No separation between 'USE' statement and its specifiers
        if line[0].isalnum():
            return None
        line = line.lstrip()
        idx = line.find("::")
        nature = None
        dcolon = None
        if idx != -1:
            # The nature of the module ("intrinsic" or
            # "non-intrinsic") is specified
            dcolon = "::"
            if line.startswith(","):
                line_nat = line[1:idx].strip()
                # Missing Module_Nature between ',' and '::'
                if not line_nat:
                    return None
                nature = Module_Nature(line_nat)
            line = line[idx + 2 :].lstrip()
            # No Module_Name after 'USE, Module_Nature ::'
            if not line:
                return None
        else:
            # Check for missing '::' after Module_Nature
            items = re.findall(r"[\w']+", line)
            for item in items:
                try:
                    nature = Module_Nature(item)
                except NoMatchError:
                    pass
            # Missing '::' after Module_Nature
            if nature is not None:
                return

        position = line.find(",")
        if position == -1:
            return nature, dcolon, Module_Name(line), "", None
        name = line[:position].rstrip()
        # Missing Module_Name before Only_List
        if not name:
            return None
        name = Module_Name(name)
        line = line[position + 1 :].lstrip()
        # Missing 'ONLY' specification after 'USE Module_Name,'
        if not line:
            return None
        if line[:4].upper() == "ONLY":
            line = line[4:].lstrip()
            if not line:
                # Expected ':' but there is nothing after the 'ONLY'
                # specification
                return None
            if line[0] != ":":
                # Expected ':' but there is a different character
                # after the 'ONLY' specification
                return None
            line = line[1:].lstrip()
            if not line:
                # Missing Only_List after 'USE Module_Name, ONLY:'
                return nature, dcolon, name, ", ONLY:", None
            return nature, dcolon, name, ", ONLY:", Only_List(line)
        return nature, dcolon, name, ",", Rename_List(line)

    def tostr(self):
        """
        :return: parsed representation of "USE" statement
        :rtype: string
        :raises InternalError: if items array is not the expected size
        :raises InternalError: if items array[2] is not a string or is an \
                               empty string
        :raises InternalError: if items array[3] is 'None' as it should be \
                               a string
        """
        if len(self.items) != 5:
            raise InternalError(
                "Use_Stmt.tostr(). 'Items' should be of size 5 but found "
                "'{0}'.".format(len(self.items))
            )
        if not self.items[2]:
            raise InternalError(
                "Use_Stmt.tostr(). 'Items' entry 2 should "
                "be a module name but it is empty"
            )
        if self.items[3] is None:
            raise InternalError(
                "Use_Stmt.tostr(). 'Items' entry 3 should "
                "be a string but found 'None'"
            )
        usestmt = "USE"
        # Add optional Module_Nature ("INTRINSIC" or "NON_INTRINSIC")
        # followed by a double colon to "USE" statement
        if self.items[0] and self.items[1]:
            usestmt += ", {0} {1}".format(self.items[0], self.items[1])
        # Add optional double colon after "USE" statement without
        # Module_Nature (valid Fortran)
        elif not self.items[0] and self.items[1]:
            usestmt += " {0}".format(self.items[1])
        # Add Module_Name and optional "ONLY" specifier if present
        usestmt += " {0}{1}".format(self.items[2], self.items[3])
        # Add optional Only_List or Rename_List if present
        if self.items[4] is not None:
            usestmt += " {0}".format(self.items[4])
        return usestmt
