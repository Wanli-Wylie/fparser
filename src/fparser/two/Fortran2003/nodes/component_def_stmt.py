from fparser.two.utils import (
    Base,
)

class Component_Def_Stmt(Base):  # R439
    """
    ::

        <component-def-stmt> is <data-component-def-stmt>
                             or <proc-component-def-stmt>

    """

    subclass_names = ["Data_Component_Def_Stmt", "Proc_Component_Def_Stmt"]
