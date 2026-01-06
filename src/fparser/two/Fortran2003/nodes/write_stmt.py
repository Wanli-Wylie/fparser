from io_control_spec_list import Io_Control_Spec_List
from output_item import Output_Item_List

class Write_Stmt(StmtBase):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R911.

    Specifies the syntax of a "WRITE" statement::

        write-stmt is WRITE ( io-control-spec-list ) [ output-item-list ]

    """

    subclass_names = []
    use_names = ["Io_Control_Spec_List", "Output_Item_List"]

    @staticmethod
    def match(string):
        """
        :param str string: Fortran code to check for a match
        :return: 2-tuple containing strings and instances of the classes
                 describing "WRITE" statement (mandatory IO control
                 specification list and optional output item list.
        :rtype: 2-tuple of objects (1 mandatory and 1 optional)
        """
        if string[:5].upper() != "WRITE":
            return
        line = string[5:].lstrip()
        # Look for mandatory IO control specification list and
        # return without a match if it is not found
        if not line.startswith("("):
            return
        line, repmap = string_replace_map(line)
        i = line.find(")")
        if i == -1:
            return
        tmp = line[1:i].strip()
        if not tmp:
            return
        tmp = repmap(tmp)
        if i == len(line) - 1:
            return Io_Control_Spec_List(tmp), None
        # Return optional output item list as well
        return (
            Io_Control_Spec_List(tmp),
            Output_Item_List(repmap(line[i + 1 :].lstrip())),
        )

    def tostr(self):
        """
        :return: parsed representation of a "WRITE" statement
        :rtype: str
        """
        if self.items[1] is None:
            return "WRITE(%s)" % (self.items[0])
        return "WRITE(%s) %s" % tuple(self.items)
