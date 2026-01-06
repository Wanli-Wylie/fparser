from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
    SequenceBase,
)
from fparser.two.utils import (
    InternalError,
)

from cray_pointee_decl import Cray_Pointee_Decl
from name import Cray_Pointee_Name
from name import Cray_Pointer_Name

class Cray_Pointer_Decl(Base):  # pylint: disable=invalid-name
    """
    ::

        cray-pointer-decl is ( cray-pointer-name, cray-pointee-decl )

    """

    use_names = ["Cray_Pointer_Name", "Cray_Pointee_Name", "Cray_Pointee_Decl"]

    @staticmethod
    def match(string):
        """Implements the matching for a Cray-pointer declaration.

        :param str string: the string to match as a Cray-pointer \
        declaration.
        :return: None if there is no match, otherwise a tuple of size \
        2 containing the name of the pointer as the first argument and \
        either the name of the pointee as the second argument or a \
        Cray-pointee declaration.
        :rtype: None, (Name, Name) or (Name, Cray_Pointee_Decl)

        """
        if not string:
            return None
        strip_string = string.strip()
        if not strip_string:
            return None
        if not strip_string[0] == "(":
            return None
        if not strip_string[-1] == ")":
            return None
        strip_string_nobr = strip_string[1:-1].strip()
        line, repmap = string_replace_map(strip_string_nobr)
        split_list = line.split(",")
        if len(split_list) != 2:
            return None
        pointer_name = repmap(split_list[0]).strip()
        pointee_str = repmap(split_list[1]).strip()
        if pointee_str[-1] == ")":
            return Cray_Pointer_Name(pointer_name), Cray_Pointee_Decl(pointee_str)
        return Cray_Pointer_Name(pointer_name), Cray_Pointee_Name(pointee_str)

    def tostr(self):
        """
        :return: this Cray-pointee declaration as a string
        :rtype: str

        :raises InternalError: if the internal items list variable is \
        not the expected size.
        :raises InternalError: if the first element of the internal \
        items list is None or is empty.
        :raises InternalError: if the second element of the internal \
        items list is None or is empty.
        """
        if len(self.items) != 2:
            raise InternalError(
                "Cray_Pointer_Decl.tostr(). 'Items' should be of size 2 but "
                "found '{0}'.".format(len(self.items))
            )
        if not self.items[0]:
            raise InternalError(
                "Cray_Pointer_Decl_Stmt.tostr(). 'Items' "
                "entry 0 should be a pointer name but it is "
                "empty"
            )
        if not self.items[1]:
            raise InternalError(
                "Cray_Pointer_Decl_Stmt.tostr(). 'Items' "
                "entry 1 should be a pointee name or pointee "
                "declaration but it is empty"
            )
        return "({0}, {1})".format(self.items[0], self.items[1])


class Cray_Pointer_Decl_List(SequenceBase):
    subclass_names = ["Cray_Pointer_Decl"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Cray_Pointer_Decl, string)

    def __iter__(self):
        return iter(self.items)
