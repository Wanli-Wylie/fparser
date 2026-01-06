from fparser.two.utils import (
    Base,
)

class Component_Data_Source(Base):  # R459
    """
    ::

        <component-data-source> = <expr>
                                  | <data-target>
                                  | <proc-target>

    """

    subclass_names = ["Proc_Target", "Data_Target", "Expr"]
