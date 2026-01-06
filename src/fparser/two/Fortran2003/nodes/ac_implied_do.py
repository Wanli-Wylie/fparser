from fparser.common.splitline import string_replace_map
from fparser.two.utils import (
    Base,
)

from ac_implied_do_control import Ac_Implied_Do_Control
from ac_value import Ac_Value_List

class Ac_Implied_Do(Base):
    """
    Fortran2003 rule R470.
    Describes the form of implicit do loop used within an array constructor::

        ac-implied-do is ( ac-value-list , ac-implied-do-control )

    Subject to the following constraint::

        C497 (R470) The ac-do-variable of an ac-implied-do that is in another
              ac-implied-do shall not appear as the ac-do-variable of the
              containing ac-implied-do.

    C497 is currently not checked - issue #257.

    """

    subclass_names = []
    use_names = ["Ac_Value_List", "Ac_Implied_Do_Control"]

    @staticmethod
    def match(string: str):
        """
        Attempts to match the supplied string as an implicit do within an
        array constructor.

        :param string: the text to match against.

        :returns: a tuple describing the match or None if there is no match.
        :rtype: Optional[Tuple[Ac_Value_List, Ac_Implied_Do_Control]]

        """
        if string[0] + string[-1] != "()":
            return None
        line, repmap = string_replace_map(string[1:-1].strip())
        i = line.rfind("=")
        if i == -1 or (i > 0 and line[i - 1] == "="):
            # No "=" or it is "==" so no match.
            return None
        j = line[:i].rfind(",")
        assert j != -1
        s1 = repmap(line[:j].rstrip())
        s2 = repmap(line[j + 1 :].lstrip())
        return Ac_Value_List(s1), Ac_Implied_Do_Control(s2)

    def tostr(self):
        return "(%s, %s)" % tuple(self.items)
