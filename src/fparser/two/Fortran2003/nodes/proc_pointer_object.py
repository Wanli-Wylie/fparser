from fparser.two.utils import (
    Base,
)

class Proc_Pointer_Object(Base):  # R740
    """
    ::

        <proc-pointer-object> = <proc-pointer-name>
                              | <proc-component-ref>

    """

    subclass_names = ["Proc_Pointer_Name", "Proc_Component_Ref"]
