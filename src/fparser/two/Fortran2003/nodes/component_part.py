from fparser.two.utils import (
    BlockBase,
)
from fparser.two.utils import (
    NoMatchError,
)

from component_def_stmt import Component_Def_Stmt

class Component_Part(BlockBase):  # R438
    """
    ::

        <component-part> is [ <component-def-stmt> ]...

    """

    subclass_names = []
    use_names = ["Component_Def_Stmt"]

    @staticmethod
    def match(reader):
        content = []
        while 1:
            try:
                obj = Component_Def_Stmt(reader)
            except NoMatchError:
                obj = None
            if obj is None:
                break
            content.append(obj)
        if content:
            return (content,)
        return None

    def tofortran(self, tab="", isfix=None):
        """
        Converts this node (and all children) into Fortran.

        :param str tab: white space to prefix to output.
        :param bool isfix: whether or not to generate fixed-format output.

        :returns: Fortran code.
        :rtype: str

        """
        mylist = []
        for item in self.content:
            mylist.append(item.tofortran(tab=tab, isfix=isfix))
        return "\n".join(mylist)
