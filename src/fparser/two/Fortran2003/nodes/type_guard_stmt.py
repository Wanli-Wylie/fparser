from fparser.two.utils import (
    StmtBase,
)

from name import Select_Construct_Name
from type_spec import Type_Spec

class Type_Guard_Stmt(StmtBase):  # R823
    """Fortran 2003 rule R823

    type-guard-stmt is TYPE IS ( type-spec ) [ select-construct-name ]
                    or CLASS IS ( type-spec ) [ select-construct-name ]
                    or CLASS DEFAULT [ select-construct-name ]

    The `items` attribute for this class will contain:

    ({'TYPE IS', 'CLASS IS', 'CLASS DEFAULT'}, Type_Spec,
    Select_Construct_Name)

    """

    subclass_names = []
    use_names = ["Type_Spec", "Select_Construct_Name"]

    @staticmethod
    def match(string):
        """Implements the matching of a Type_Guard_Stmt rule.

        :param str string: the code that we are trying to match.

        :returns: a 3-tuple, containing the guard rule as a string (one of
            'TYPE IS', 'CLASS IS' or 'CLASS DEFAULT'),
            followed by an optional Type_Spec and an optional
            Select_Construct_Name. Returns None if there is no match.
        :rtype: Optional[Tuple[str, Optional[:py:class:`fparser.two.Type_Spec`],
            Optional[:py:class:`fparser.two.Select_Construct_Name`]]]

        """
        string = string.lstrip()
        if string[:4].upper() == "TYPE":
            line = string[4:].lstrip()
            if not line[:2].upper() == "IS":
                return None
            line = line[2:].lstrip()
            kind = "TYPE IS"
        elif string[:5].upper() == "CLASS":
            line = string[5:].lstrip()
            if line[:2].upper() == "IS":
                line = line[2:].lstrip()
                kind = "CLASS IS"
            elif line[:7].upper() == "DEFAULT":
                line = line[7:].lstrip()
                if line:
                    return "CLASS DEFAULT", None, Select_Construct_Name(line)
                return "CLASS DEFAULT", None, None
            else:
                return None
        else:
            return None
        if not line.startswith("("):
            return None
        index = line.rfind(")")
        if index == -1:
            return None
        tmp = line[1:index].strip()
        if not tmp:
            return None
        line = line[index + 1 :].lstrip()
        if line:
            return kind, Type_Spec(tmp), Select_Construct_Name(line)
        return kind, Type_Spec(tmp), None

    def tostr(self):
        """
        :returns: string containing Fortran code for the parsed
            Type_Guard_Stmt rule.
        :rtype: str

        """
        string = str(self.items[0])
        if self.items[1] is not None:
            string += f" ({self.items[1]})"
        if self.items[2] is not None:
            string += f" {self.items[2]}"
        return string

    def get_end_name(self):
        """
        :returns: the name at the END of this block, if it exists,
            otherwise None.
        :rtype: Optional[str]

        """
        name = self.items[-1]
        if name is not None:
            return name.string
        return None
