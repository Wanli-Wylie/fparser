from fparser.two.utils import (
    EndStmtBase,
)

from generic_spec import Generic_Spec

class End_Interface_Stmt(EndStmtBase):  # R1204
    """
    ::

        <end-interface-stmt> = END INTERFACE [ <generic-spec> ]

    Attributes::

        items : (Generic_Spec, )

    """

    subclass_names = []
    use_names = ["Generic_Spec"]

    @staticmethod
    def match(string):
        return EndStmtBase.match(
            "INTERFACE", Generic_Spec, string, require_stmt_type=True
        )
