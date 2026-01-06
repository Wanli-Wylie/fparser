from fparser.two.utils import (
    Base,
)

class Actual_Arg(Base):  # R1221
    """
    ::

        <actual-arg> = <expr>
                     | <variable>
                     | <procedure-name>
                     | <proc-component-ref>
                     | <alt-return-spec>

    """

    subclass_names = [
        "Expr",
        "Procedure_Name",
        "Proc_Component_Ref",
        "Alt_Return_Spec",
        "Variable",
    ]
