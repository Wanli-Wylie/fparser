from fparser.two.utils import (
    Base,
)

class Proc_Language_Binding_Spec(Base):  # 1225
    """
    <proc-language-binding-spec> = <language-binding-spec>
    """

    subclass_names = ["Language_Binding_Spec"]
