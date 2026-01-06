from cray_pointer_decl import Cray_Pointer_Decl_List

class Cray_Pointer_Stmt(StmtBase, WORDClsBase):  # pylint: disable=invalid-name
    """
    ::

        cray-pointer-stmt is POINTER cray-pointer-decl-list

    """

    subclass_names = []
    use_names = ["Cray_Pointer_Decl_List"]

    @staticmethod
    def match(string):
        """Implements the matching for a Cray-pointer statement.

        :param string: the reader or string to match as a Cray-pointer \
                       statement.
        :type string: \
        :py:class:`fparser.common.readfortran.FortranReaderBase` or \
        `str`
        :return: a tuple of size 2 containing a string with the name \
        "POINTER" and a cray-pointer-decl-list, if there is a match, \
        or `None` if there is not.
        :rtype: (str, Cray_Pointer_Decl_List) or None

        """
        if "cray-pointer" not in EXTENSIONS():
            return None
        return WORDClsBase.match(
            "POINTER", Cray_Pointer_Decl_List, string, require_cls=True
        )
