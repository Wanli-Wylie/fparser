from fparser.two.utils import (
    Base,
)

class Component_Array_Spec(Base):  # R443
    """
    ::

        <component-array-spec> = <explicit-shape-spec-list>
                                 | <deferred-shape-spec-list>

    """

    subclass_names = ["Explicit_Shape_Spec_List", "Deferred_Shape_Spec_List"]
