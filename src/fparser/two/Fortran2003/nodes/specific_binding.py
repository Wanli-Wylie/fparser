from fparser.two.utils import (
    StmtBase,
)
from fparser.two.utils import (
    InternalError,
)

from binding_attr import Binding_Attr_List
from interface_name import Interface_Name
from name import Binding_Name
from name import Procedure_Name

class Specific_Binding(StmtBase):  # pylint: disable=invalid-name
    """Fortran2003 Rule R451::

        <specific-binding> = PROCEDURE [ ( <interface-name> ) ] [
            [ , <binding-attr-list> ] :: ] <binding-name> [ => <procedure-name> ]

    Specifies the syntax of specific binding for a type-bound
    procedure within a derived type.

    The following are associated constraints::

        C456 (R451) If => procedure-name appears, the double-colon
        separator shall appear.

        C457 (R451) If => procedure-name appears, interface-name shall not
        appear.

        C458 (R451) The procedure-name shall be the name of an accessible
        module procedure or an external procedure that has an explicit
        interface. Note, this is not checked by fparser.

    """

    subclass_names = []
    use_names = [
        "Interface_Name",
        "Binding_Attr_List",
        "Binding_Name",
        "Procedure_Name",
    ]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: 5-tuple containing strings and instances of the classes
                 describing a specific type-bound procedure (optional
                 interface name, optional binding attribute list,
                 optional double colon delimiter, mandatory binding
                 name and optional procedure name)
        :rtype: 5-tuple of objects (1 mandatory and 4 optional)
        """
        # Remove any leading, trailing spaces.
        string_strip = string.strip()
        if string_strip[:9].upper() != "PROCEDURE":
            # There is no 'PROCEDURE' statement.
            return None
        if len(string_strip) < 11:
            # Line is too short to be valid
            return None
        # Remember whether there was a space after the keyword
        space_after = False
        if string_strip[9] == " ":
            space_after = True
        line = string_strip[9:].lstrip()
        # Find optional interface name if it exists.
        iname = None
        if line.startswith("("):
            index = line.find(")")
            if index == -1:
                # Left brace has no corresponding right brace
                return None
            iname = Interface_Name(line[1:index].strip())
            line = line[index + 1 :].lstrip()
        # Look for optional double colon and binding attribute list.
        dcolon = None
        mylist = None
        index = line.find("::")
        if index != -1:
            dcolon = "::"
            if line.startswith(","):
                mylist = Binding_Attr_List(line[1:index].strip())
            elif line[:index].strip():
                # There is content between procedure (with optional
                # interface) and :: that does not start with a ','
                # which is a syntax error.
                return None
            line = line[index + 2 :].lstrip()
        if not iname and not dcolon:
            # there is no interface name or double colon between the
            # keyword and the binding name. Therefore we expect a
            # space between the two.
            if not space_after:
                # No space was found so return to indicate an
                # error.
                return None
        # Find optional procedure name.
        index = line.find("=>")
        pname = None
        if index != -1:
            pname = Procedure_Name(line[index + 2 :].lstrip())
            line = line[:index].rstrip()
            if not dcolon:
                # Constraint C456 requires '::' if there is a
                # procedure-name.
                return None
        if iname and pname:
            # Constraint C457 disallows interface-name if there is a
            # procedure-name.
            return None
        # Return class arguments.
        return iname, mylist, dcolon, Binding_Name(line), pname

    def tostr(self):
        """
        :return: parsed representation of a specific type-bound procedure
        :rtype: `str`

        """
        if len(self.items) != 5:
            raise InternalError(
                "Class Specific_Binding method tostr() has '{0}' items, "
                "but expecting 5.".format(len(self.items))
            )

        stmt = "PROCEDURE"
        # Add optional interface name
        if self.items[0]:
            stmt += "({0})".format(self.items[0])
        # Add optional double colon and binding attribute list
        # (if the list is present)
        if self.items[1] and self.items[2]:
            stmt += ", {0} {1}".format(self.items[1], self.items[2])
        elif not self.items[1] and self.items[2]:
            stmt += " {0}".format(self.items[2])
        # Add mandatory Binding_Name
        stmt += " {0}".format(self.items[3])
        # Add optional procedure name
        if self.items[4]:
            stmt += " => {0}".format(self.items[4])
        return stmt
