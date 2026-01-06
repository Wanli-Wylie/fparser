from derived_type_spec import Derived_Type_Spec

class Dtv_Type_Spec(CALLBase):  # R920
    """
    ::

        <dtv-type-spec> = TYPE ( <derived-type-spec> )
                          | CLASS ( <derived-type-spec> )

    """

    subclass_names = []
    use_names = ["Derived_Type_Spec"]

    @staticmethod
    def match(string):
        return CALLBase.match(
            ["TYPE", "CLASS"], Derived_Type_Spec, string, require_rhs=True
        )
