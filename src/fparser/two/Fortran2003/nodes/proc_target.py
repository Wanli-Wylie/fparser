from fparser.two.utils import (
    Base,
)

class Proc_Target(Base):  # R742
    """
    ::

        <proc-target> = <expr>
                        | <procedure-name>
                        | <proc-component-ref>

    """

    subclass_names = ["Proc_Component_Ref", "Procedure_Name", "Expr"]
