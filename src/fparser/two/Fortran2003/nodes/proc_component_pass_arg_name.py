from name import Arg_Name

class Proc_Component_PASS_Arg_Name(CALLBase):
    """
    ::

        <proc-component-PASS-arg-name> = PASS ( <arg-name> )

    """

    subclass_names = []
    use_names = ["Arg_Name"]

    @staticmethod
    def match(string):
        return CALLBase.match("PASS", Arg_Name, string)
